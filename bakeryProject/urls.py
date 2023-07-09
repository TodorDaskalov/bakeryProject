from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bakeryProject.bakery_main.urls')),
    path('products/', include('bakeryProject.products.urls')),
    path('cart/', include('bakeryProject.cart.urls'))
]
