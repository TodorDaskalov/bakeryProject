from django.shortcuts import render, redirect
from bakeryProject.orders.models import Order


def show_orders(request):

    orders = Order.objects.exclude(status='Done').order_by('pickup_time')
    received_orders = orders.filter(status='received')
    working_on_it_orders = orders.filter(status='working')
    ready_orders = orders.filter(status='ready_to_pickup')

    context = {
        'orders': orders,
        'received_orders': received_orders,
        'working_on_it_orders': working_on_it_orders,
        'ready_orders': ready_orders
    }

    return render(request, 'orders/staff_orders.html', context)


def update_order(request, pk):

    order = Order.objects.get(pk=pk)

    if order.status == 'received':
        order.status = 'working'
    elif order.status == 'working':
        order.status = 'ready_to_pickup'
    elif order.status == 'ready_to_pickup':
        order.status = 'done'

    order.save()

    return redirect('show_orders')
