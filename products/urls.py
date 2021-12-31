from django.urls import path
from .views import *

urlpatterns = [
  path( "product_list", product_list, name="product_list"),
  path("product-details/<int:id>/", single_product, name="single_product")
]
