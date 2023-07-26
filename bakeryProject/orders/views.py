from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from bakeryProject.orders.forms import CustomOrderForm
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


@login_required
def custom_order(request):
    if request.method == 'POST':
        form = CustomOrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            email = form.cleaned_data['email']
            order_text = form.cleaned_data['order_text']

            subject = f"Custom Order Question from {email}"
            message = f"Customer Name: {customer_name}\nEmail: {email}\nOrder Details: {order_text}"
            from_email = "anchisbakery02@gmail.com"
            to_email = ["anchisbakery02@gmail.com"]

            send_mail(subject, message, from_email, to_email)

            return render(request, 'orders/custom_order_success.html')
    else:
        form = CustomOrderForm(initial={'user': request.user})

    return render(request, 'orders/custom_order.html', {'form': form})
