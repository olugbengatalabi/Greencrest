from django.urls import path
from .views import *
urlpatterns = [
  path("", cart, name="cart"),
  path('add-to-cart/<int:id>/', add_to_cart, name ='add-to-cart'),
  path('remove-from-cart/<int:id>/', remove_from_cart, name ='remove-from-cart'),
  path('remove-from-cart-page/<int:id>/', remove_from_cart_page, name ='remove-from-cart-page'),
]
