from django.contrib import messages
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from products.models import Product

from cart.models import Cart, CartItem


@login_required (login_url = "account_login")
def add_to_cart(request, id ):
  if request.method == "POST":
    quantity = int(request.POST["quantity"])
  else:
    quantity = 1
  product = get_object_or_404(Product, id = id)
  if product.discount_price is not None:
    price = product.discount_price
  else:
    price = product.price
  line_total = quantity * price
  cart, new_cart = Cart.objects.get_or_create(user = request.user, ordered = False )
  cart_item, created = CartItem.objects.get_or_create(user = request.user, product = product, ordered = False, price = price, quantity = quantity, line_total = line_total)
  if created:
    cart.cart_items.add(cart_item)
    cart.save()
    messages.success(request, 'Added')
  else:
    messages.error(request, "Already in your cart")

  if "product-details" in request.META.get('HTTP_REFERER'):
    return redirect("single_product", id = id)
  elif "product_list" in request.META.get('HTTP_REFERER'):
    return redirect("product_list")
  else:
    return redirect("index")


@login_required (login_url = "account_login")
def remove_from_cart(request, id):
  product = get_object_or_404(Product, id = id)
  cart_qs = Cart.objects.filter(user = request.user, ordered = False)
  if cart_qs.exists():
    cart = cart_qs[0]
    if cart.cart_items.filter(product = product).exists():
      cart_item = CartItem.objects.filter(product = product, user = request.user, ordered = False)
      cart_item.delete()
      messages.info(request, 'removed')
  return redirect("single_product", id = id)

def remove_from_cart_page(request, id):
  cart_item = CartItem.objects.filter(id = id)
  cart_item.delete()
  messages.info(request, "Deleted")
  return redirect("cart")


@login_required(login_url = "account_login")
def clear_cart(request):
    cart = Cart.objects.get(user =request.user, ordered = False)
    cart.cart_items.delete
    
@login_required (login_url = "account_login")
def cart(request):
  try:
    cart = Cart.objects.get( user = request.user, ordered = False)
    total = 0
    cart_items = cart.cart_items.all()
    for item in cart_items:
      total+= item.line_total
    cart.total = total
    cart.save()
    if cart_items.count() != 0:
      context = {
        "cart_items":cart_items,
        "cart_total": total
      }
    else:
      messages.info(request, "Empty")
      return redirect("/")  
  except Cart.DoesNotExist:
    messages.error(request, "Empty, add a product to cart now")
    return redirect("/")
  return render(request, "cart/cart2.html", context)