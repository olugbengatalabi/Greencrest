from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("payment/", include("payment.urls")),
    path('accounts/', include('allauth.urls')),
    path("", include("pages.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
