from django.shortcuts import render, redirect

from bakeryProject.orders.models import Order


def show_orders(request):

    orders = Order.objects.exclude(status='Done').order_by('pickup_time')

    context = {
        'orders': orders
    }

    return render(request, 'orders/staff_orders.html', context)


def update_order(request, pk):

    order = Order.objects.get(pk=pk)

    if order.status == 'Received':
        order.status = 'Working on it'
    elif order.status == 'Working on it':
        order.status = 'Ready to pickup'
    elif order.status == 'Ready to pickup':
        order.status = 'Done'

    order.save()

    return redirect('show_orders')
