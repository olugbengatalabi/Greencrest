from django.contrib import admin
from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
  list_display = ["product","price", "line_total", "ordered","user"]
  list_display_links = ["product", "user"]
  list_filter = ["price", "product", "line_total"]
  
class CartAdmin(admin.ModelAdmin):
  list_display = ["user","start_date", "ordered", "total","coupon", "being_delivered", "refund_requested", "refund_granted"]
  list_display_links = [ "user"]
  list_filter = ["user", "ordered", "coupon", "refund_requested"]
  
admin.site.register(Cart)
admin.site.register(CartItem)