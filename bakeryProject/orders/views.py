from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from bakeryProject.bakery_main.models import Profile
from bakeryProject.orders.forms import CustomOrderForm
from bakeryProject.orders.models import Order


@login_required()
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


@login_required()
def update_order(request, pk):

    order = Order.objects.get(pk=pk)
    products = order.products
    user = order.user
    customer_name = str(Profile.objects.filter(user=user).first())
    customer_name = customer_name.replace('None', '').strip()
    if customer_name:
        name = customer_name
    else:
        name = user.email

    if order.status == 'received':
        order.status = 'working'

    elif order.status == 'working':
        order.status = 'ready_to_pickup'
        subject = 'Your Order is Ready for Pickup'
        from_email = 'anchisbakery02@gmail.com'
        to_email = [order.user.email]

        context = {'order': order,
                   'products': products,
                   'name': name}

        html_message = render_to_string('orders/order_ready.html', context)
        plain_message = strip_tags(html_message)

        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

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
