from django.urls import path
from bakeryProject.products.views import ProductListView, ProductDetailView, CategoryProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:category>/', CategoryProductListView.as_view(), name='category_products'),
]
