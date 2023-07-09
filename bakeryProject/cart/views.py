from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from bakeryProject.cart.models import CartItem, Cart


class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    fields = ['product', 'quantity']
    login_url = 'login_user'

    def form_valid(self, form):
        form.instance.cart = self.request.user.cart
        form.save()
        #TODO After adding the product to the cart stay on the same place
        return redirect(self.request.META['HTTP_REFERER'])


def cart_view(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    return render(request, 'cart/cart.html', {'cart_items': cart_items})
