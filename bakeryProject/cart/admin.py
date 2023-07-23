from django.contrib import admin


from bakeryProject.cart.models import CartItem, Cart


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    ordering = ('user', 'created_at')
    list_filter = ('user', 'created_at')


@admin.register(CartItem)
class AdminCartItem(admin.ModelAdmin):
    list_display = ('cart', 'product')
    ordering = ('cart', 'product')
    list_filter = ('cart', 'product')
