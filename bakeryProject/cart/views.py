from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
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

    total_price = 0
    for item in cart.items.all():
        total_price += item.product.price * item.quantity

    form = OrderForm()

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['pickup_time'] != 'now':
                pickup_time_str = form.cleaned_data['pickup_time']
                pickup_time = datetime.strptime(pickup_time_str, '%H:%M')
            else:
                pickup_time = datetime.now()
                pickup_time = pickup_time.strftime('%H:%M')
                pickup_time = datetime.strptime(pickup_time, '%H:%M')
            products = []
            for item in cart.items.all():
                products.append(f'{item.product} x {item.quantity}')

            order = Order.objects.create(
                user=request.user,
                pickup_time=pickup_time,
                products=', '.join(products),
                status='Received',
                total_price=total_price)

            order.save()

            cart.items.all().delete()

            return render(request, 'cart/place_order_success.html')

    context = {
        'total_price': total_price,
        'form': form
    }

    return render(request, 'cart/place_order.html', context)
