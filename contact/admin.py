from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
  list_display = ("user", "date_sent")
  list_display_links = ["user"]
  search_fields = ("message", "user")
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
