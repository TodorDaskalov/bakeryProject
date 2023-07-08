from django.urls import path
from bakeryProject.products.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
]
