from django.shortcuts import render
from django.db.models import Avg
from .models import Customer, Order


def dashboard(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    orders = Order.objects.all()
    if start_date:
        orders = orders.filter(created_at__gte=start_date)
    if end_date:
        orders = orders.filter(created_at__lte=end_date)

    total_orders = orders.count()
    total_customers = Customer.objects.count()
    average_order_value = orders.aggregate(avg_value=Avg('value'))['avg_value']

    context = {
        'total_orders': total_orders,
        'total_customers': total_customers,
        'average_order_value': average_order_value,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'OrderApp/dashboard.html', context)
