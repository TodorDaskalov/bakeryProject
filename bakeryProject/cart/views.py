from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from bakeryProject.cart.forms import OrderForm
from bakeryProject.cart.models import CartItem, Cart


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
            # Process the cart with the objects in the staff orders page to be prepared
            return render(request, 'cart/order_success.html')

    context = {
        'total_price': total_price,
        'form': form
    }

    return render(request, 'cart/order.html', context)
