from django import template
from cart.models import Cart

register = template.Library()

@register.filter
def cart_item_count(user):
  if user.is_authenticated:
    qs = Cart.objects.filter(user= user, ordered = False)
    if qs.exists():
      return qs[0].cart_items.count()
  return 0
