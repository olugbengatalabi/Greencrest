from django.urls import path
from .views import *
from products.views import *
urlpatterns = [
  path("", index, name="index"),
]
