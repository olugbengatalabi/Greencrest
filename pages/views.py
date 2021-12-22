from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Product


def index(request):
  queryset = Product.objects.filter(featured = True)
  paginator = Paginator(queryset, 3)
  page = request.GET.get('page')
  paged_products = paginator.get_page(page)
  context = {
    "products": paged_products
  }
  return render(request, "pages/index.html", context)
