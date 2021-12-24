from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages

def message(request):
  if request.user.is_authenticated:
    
    if request.user and request.method == "POST":
      message = request.POST["message"]
      subject = request.POST["subject"]
      email = request.POST["email"]
      Contact.objects.create(message = message, subject = subject, email = email, user = request.user )
      messages.success(request, "message sent, reply will be sent to the email associated with this account")
  else:
    messages.error(request, "Login to be able to send us a message")
    return redirect("account_login")
  return redirect("index")