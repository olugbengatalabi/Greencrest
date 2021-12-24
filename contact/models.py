from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.fields import EmailField

# Create your models here.
class Contact(models.Model):
  user =  models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.EmailField()
  subject = models.CharField(max_length= 300)
  message = models.TextField(blank=True )
  date_sent = models.DateTimeField(auto_now_add=True,)
  def __str__(self):
    return self.subject
