from django.contrib import admin
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
  list_display = ["title","price", "featured", "category","quantity available"]
  list_display_links = ["title"]
  list_display_editable = ["featured"]
  
  list_filter = ["title", "price", "featured"]

class ProductImageAdmin(admin.ModelAdmin):
  list_display = ["title","product"]
  list_display_links = ["title", "product"]
  
  
admin.site.register(Product)
admin.site.register(ProductImage)

# Register your models here.
