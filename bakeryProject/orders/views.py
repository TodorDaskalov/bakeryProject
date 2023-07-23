from django.shortcuts import render, redirect
from bakeryProject.orders.models import Order


def show_orders(request):

    orders = Order.objects.exclude(status='Done').order_by('pickup_time')
    received_orders = orders.filter(status='Received')
    working_on_it_orders = orders.filter(status='Working on it')
    ready_orders = orders.filter(status='Ready to pickup')

    context = {
        'orders': orders,
        'received_orders': received_orders,
        'working_on_it_orders': working_on_it_orders,
        'ready_orders': ready_orders
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
