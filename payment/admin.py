from django.contrib import admin
from .models import Address,Payment, UserProfile, Refund, Coupon



class AddressAdmin(admin.ModelAdmin):
  list_display = ["user","address_type" ]
  list_display_links = ["user"]

class PaymentiAdmin(admin.ModelAdmin):
  list_display = ["amount", "ref", "email", "verified", "date_created"]
  list_editable = [ "featured"]
  list_filter = ["verified", "date_created"]


class CouponAdmin(admin.ModelAdmin):
  list_display = ["code","amount","active"]
  list_editable = [ "active"]
  

class RefundAdmin(admin.ModelAdmin):
  list_display = ["user","accepted", "email", "date_created"]
  list_display_links = ["user"]
  list_editable = [ "accepted"]
  list_filter = ["accepted", "date_created"]
  


admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address)
admin.site.register(Refund)
admin.site.register(UserProfile)

# Register your models here.
