from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from bakeryProject.cart.forms import OrderForm
from bakeryProject.cart.models import CartItem, Cart
from bakeryProject.orders.models import Order


class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    fields = ['product', 'quantity']
    login_url = 'login_user'

    def form_valid(self, form):
        cart = self.request.user.cart
        product = form.cleaned_data['product']
        quantity = form.cleaned_data['quantity']

        existing_item = CartItem.objects.filter(cart=cart, product=product).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            form.instance.cart = cart
            form.instance.quantity = quantity
            form.save()

        return redirect(f"{self.request.META['HTTP_REFERER']}#product-{product.pk}")


class RemoveItemView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('cart_page')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(cart=self.request.user.cart)
        return queryset


def cart_view(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    return render(request, 'cart/cart.html', {'cart_items': cart_items})


def order_products(request):
    cart = Cart.objects.get(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart.items.all())
    currency = [item.product.currency for item in cart.items.all()][0]

    form = OrderForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            pickup_time_str = form.cleaned_data['pickup_time']
            if pickup_time_str == 'now':
                pickup_time = datetime.now()
            else:
                pickup_time = datetime.now().strptime(pickup_time_str, '%H:%M')

            products = [f'{item.product} x {item.quantity}' for item in cart.items.all()]

            with transaction.atomic():
                order = Order.objects.create(
                    user=request.user,
                    pickup_time=pickup_time,
                    products=', '.join(products),
                    status='received',
                    total_price=total_price,
                    currency=currency
                )

                cart.items.all().delete()

            return render(request, 'cart/place_order_success.html')

    context = {
        'total_price': total_price,
        'currency': currency,
        'form': form
    }

    return render(request, 'cart/place_order.html', context)
