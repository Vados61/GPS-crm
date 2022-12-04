from django.http import HttpResponseRedirect
from django.shortcuts import render

from workshop.models import Order, OrderPosition


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


def workshop(request):
    orders_c = Order.objects.filter(status='готово')
    orders_n = Order.objects.filter(status='принято')
    context = {
        'orders_c': orders_c,
        'orders_n': orders_n,
        'active': 'Цех'
    }
    return render(request, 'workshop.html', context)


def finish_order(request, pk):
    count_repair = request.GET.get('rep', 0)
    order = Order.objects.get(id=pk)
    order.complite(count_repair)
    order.save()
    return HttpResponseRedirect("/workshop")


def unfinished_order(request, pk):
    order = Order.objects.get(id=pk)
    order.unfinished()
    order.save()
    return HttpResponseRedirect("/workshop")
