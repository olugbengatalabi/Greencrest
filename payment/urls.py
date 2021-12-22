from django.urls import path
from .views import *

urlpatterns = [
  path( "checkout", CheckoutView.as_view(), name="checkout"),
  path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
  path( "initiate-payment", initiate_payment, name="initiate-payment"),
  path("<str:ref>/", verify_payment, name = "verify-payment")

]
