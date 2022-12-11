from django.http import HttpResponseRedirect
from django.shortcuts import render

from workshop.models import Order, OrderPosition, Firm


def index(request):
    complite = Order.objects.values('pk').filter(status='готово').count()
    income = Order.objects.values('pk').filter(status='принято').count()
    count = 0
    pos = OrderPosition.objects.values('quantity').filter(order__status='готово')
    for q in pos:
        count += q['quantity']
    pos = OrderPosition.objects.values('quantity').filter(order__status='принято')
    for q in pos:
        count += q['quantity']
    context = {
        'complite': complite,
        'income': income,
        'count': count,
        'active': 'Главная'
    }
    return render(request, 'home.html', context)


def workshop_view(request):
    orders_c = Order.objects.filter(status='готово')
    orders_n = Order.objects.filter(status='принято')
    context = {
        'orders_c': orders_c,
        'orders_n': orders_n,
        'active': 'Цех'
    }
    return render(request, 'workshop.html', context)


def order_view(request, order_pk):
    status = request.GET.get('set_status')
    order = Order.objects.get(pk=order_pk)
    if status:
        order.set_status(status)
        order.save()
        return HttpResponseRedirect(f'/order/{order_pk}')
    context = {
        "order": order,
        'active': 'Цех',
    }
    return render(request, 'order.html', context)


def client_view(request, pk=None):
    if pk is None:
        clients = Firm.objects.all()
        context = {
            "clients": clients,
            'active': 'Клиенты',
        }
        return render(request, "clients.html", context)
    client = Firm.objects.get(id=pk)
    context = {
        "client": client,
        'active': 'Клиенты',
    }
    return render(request, "client.html", context)
