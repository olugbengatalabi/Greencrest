import secrets
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings

from cart.models import Cart
from .paystack import PayStack
from django_countries.fields import CountryField

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username



class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'
        



class Payment(models.Model):
    amount =  models.DecimalField(decimal_places = 2, max_digits = 100)
    ref = models.CharField(max_length = 200)
    email = models.EmailField()
    verified = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    class Meta: 
        ordering = ('-date_created',)
    def __str__(self) -> str:
        return f"paid: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
    def amount_value(self) -> int:
        return self.amount * 100
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:

            if round(result["amount"]/100, 2) == float(self.amount):
                self.verified = True
                self.save()
        if self.verified:
            return True
        return False
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount =  models.DecimalField(decimal_places=2, max_digits=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Refund(models.Model):
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE, verbose_name = "Relevant Cart")
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
