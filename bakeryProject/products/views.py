from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class CategoryProductListView(ListView):
    model = Product
    template_name = 'products/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)

# class AllProductsListView(ListView):
#     model = Product
#     template_name = 'all_products.html'
#     context_object_name = 'products'