from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import View

from greencrest.settings import PAYSTACK_PUBLIC_KEY

from .forms import CheckoutForm, CouponForm, RefundForm
from cart.models import CartItem, Cart
from products.models import Product
from payment.models import Address, Coupon, Payment, Refund, UserProfile

# Create your views here.
def is_valid_form(values):
    valid = True
    for field in values:
        if field == "":
            valid = False
    return valid

# @login_required(login_url="account_login")
class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                "form": form,
                "couponform": CouponForm(),
                "cart": cart,
                "DISPLAY_COUPON_FORM": True,
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user, address_type="S", default=True
            )
            if shipping_address_qs.exists():
                context.update({"default_shipping_address": shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user, address_type="B", default=True
            )
            if billing_address_qs.exists():
                context.update({"default_billing_address": billing_address_qs[0]})
            return render(self.request, "payment/checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "There are no items in your cart")
            return redirect("checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            cart = Cart.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():

                use_default_shipping = form.cleaned_data.get("use_default_shipping")
                if use_default_shipping:
                    address_qs = Address.objects.filter(
                        user=self.request.user, address_type="S", default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        cart.shipping_address = shipping_address
                        cart.save()
                    else:
                        messages.info(
                            self.request, "No default shipping address available"
                        )
                        return redirect("checkout")
                else:
                    shipping_address1 = form.cleaned_data.get("shipping_address")
                    shipping_address2 = form.cleaned_data.get("shipping_address2")
                    shipping_country = form.cleaned_data.get("shipping_country")
                    shipping_zip = form.cleaned_data.get("shipping_zip")

                    if is_valid_form(
                        [shipping_address1, shipping_country, shipping_zip]
                    ):
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            address_type="S",
                        )
                        shipping_address.save()

                        cart.shipping_address = shipping_address
                        cart.save()

                        set_default_shipping = form.cleaned_data.get(
                            "set_default_shipping"
                        )
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()

                    else:
                        messages.info(
                            self.request,
                            "Please fill in the required address fields",
                        )
                        return redirect("checkout")

                use_default_billing = form.cleaned_data.get("use_default_billing")
                same_billing_address = form.cleaned_data.get("same_billing_address")

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = "B"
                    billing_address.save()
                    cart.billing_address = billing_address
                    cart.save()

                elif use_default_billing:
                    address_qs = Address.objects.filter(
                        user=self.request.user, address_type="B", default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        cart.billing_address = billing_address
                        cart.save()
                    else:
                        messages.info(
                            self.request, "No default billing address available"
                        )
                        return redirect("checkout")
                else:
                    billing_address1 = form.cleaned_data.get("billing_address")
                    billing_address2 = form.cleaned_data.get("billing_address2")
                    billing_country = form.cleaned_data.get("billing_country")
                    billing_zip = form.cleaned_data.get("billing_zip")

                    if is_valid_form([billing_address1, billing_country, billing_zip]):
                        billing_address = Address(
                            user=self.request.user,
                            street_address=billing_address1,
                            apartment_address=billing_address2,
                            country=billing_country,
                            zip=billing_zip,
                            address_type="B",
                        )
                        billing_address.save()

                        cart.billing_address = billing_address
                        cart.save()

                        set_default_billing = form.cleaned_data.get(
                            "set_default_billing"
                        )
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request,
                            "Please fill in the required address fields",
                        )
                        return redirect("checkout")

                # payment_option = form.cleaned_data.get("payment_option")
                return redirect("initiate-payment")
            
                # if payment_option == "S":
                #     return redirect("payment", payment_option="stripe")
                # elif payment_option == "P":
                #     return redirect("payment", payment_option="paystack")
                # else:
                #     messages.warning(self.request, "Invalid payment option selected")
                #     return redirect("checkout")
        except ObjectDoesNotExist:
            messages.warning(self.request, "Cannot pay for an empty cart")
            return redirect("/")


def get_coupon(request, code, cart):
    try:
        coupon = Coupon.objects.get(code=code)
        messages.success(request, "Successfully added coupon")
        cart.coupon = coupon
        cart.save()
    except ObjectDoesNotExist:
        messages.error(request, "This coupon does not exist")
        return redirect("checkout")
    # amount = coupon.amount
    # new_total = cart.total - amount
    # cart.total = new_total


class AddCouponView(View):
    
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get("code")
                cart = Cart.objects.get(user=self.request.user, ordered=False)
                if cart:
                    try:
                        coupon = Coupon.objects.get(code=code)
                        messages.success(self.request, "Successfully added coupon")
                        cart.coupon = coupon
                        cart.save()
                    except ObjectDoesNotExist:
                        messages.error(self.request, "This coupon does not exist")
                        return redirect("checkout")

                    amount = coupon.amount
                    new_total = cart.total - amount
                    cart.total = new_total
                    cart.save()


                return redirect("checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("checkout")
        else:
            messages.error(self.request, "Not a valid coupon code")
            return redirect("checkout")

@login_required(login_url="account_login")
def initiate_payment(request):
    cart = Cart.objects.get(user = request.user, ordered = False)
    payment = Payment.objects.create(amount = cart.total, email = request.user.email, )
    context = {
        "payment": payment,
            
        "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY
        }
    return render(request, "payment/make_payment.html", context)
        
@login_required(login_url="account_login")
def verify_payment(request, ref):
    cart = get_object_or_404(Cart, user = request.user)
    payment = get_object_or_404(Payment, ref = ref)
    verified = payment.verify_payment()
    if verified:
        cart.ordered = True
        cart_items = CartItem.objects.filter(user = request.user)
        for item in cart_items:
            item.ordered = True
            item.save()
        cart.save()
        messages.success(request, "Verification Successful, continue shopping")
    else:
        messages.error(request, "verification failed, contact support for more details")
    return redirect("/")

