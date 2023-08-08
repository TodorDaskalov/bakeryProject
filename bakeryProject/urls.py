from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

from bakeryProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bakeryProject.bakery_main.urls')),
    path('products/', include('bakeryProject.products.urls')),
    path('cart/', include('bakeryProject.cart.urls')),
    path('orders/', include('bakeryProject.orders.urls')),
    path('404/', page_not_found, {'template_name': '404.html'}, name='404')
]
