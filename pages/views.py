from django.core.paginator import Paginator
from django.db.models import query
from django.shortcuts import render
from products.models import Product


def index(request):
  print('bbb' + request.path)
  queryset = Product.objects.filter(featured = True, display_on_homepage = True)[:6]
  context = {
    "products" : queryset
  }
  return render(request, "pages/index.html", context)
