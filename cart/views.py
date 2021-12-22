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

    product = get_object_or_404(Product, id = id)
    if product.discount_price is not None:
      price = product.discount_price
    else:
      price = product.price
    line_total = quantity * price
    cart, new_cart = Cart.objects.get_or_create(user = request.user, ordered = False )
    cart_item = CartItem.objects.create(user = request.user, product = product, ordered = False, price = price, quantity = quantity, line_total = line_total)
    cart.cart_items.add(cart_item)
    cart.save()
    messages.info(request, 'Added to cart')
    return redirect("single_product", id = id)
  else:
    return redirect("single_product", id=id)

@login_required (login_url = "account_login")
def remove_from_cart(request, id):
  product = get_object_or_404(Product, id = id)
  cart_qs = Cart.objects.filter(user = request.user, ordered = False)
  if cart_qs.exists():
    cart = cart_qs[0]
    if cart.cart_items.filter(product = product).exists():
      cart_item = CartItem.objects.filter(product = product, user = request.user, ordered = False)
      cart_item.delete()
      messages.info(request, 'removed from cart')
  return redirect("single_product", id = id)

def remove_from_cart_page(request, id):
  cart_item = CartItem.objects.filter(id = id)
  cart_item.delete()
  messages.info(request, "Deleted from cart")
  return redirect("cart")


@login_required(login_url = "account_login")
def clear_cart(request):
    cart = Cart.objects.get(user =request.user, ordered = False)
    cart.cart_items.delete
    
@login_required (login_url = "account_login")
def cart(request):
  try:
    cart = Cart.objects.get( user = request.user, ordered = False)
    total = 0.00
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
      messages.info(request, "Cart is empty")
      return redirect("/")  
  except Cart.DoesNotExist:
    messages.error(request, "Cart is empty")
    return redirect("/")
  return render(request, "cart/cart.html", context)