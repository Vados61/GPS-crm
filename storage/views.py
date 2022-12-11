from django.forms import modelformset_factory
from django.shortcuts import render

# from storage.forms import PositionForm
from storage.models import Stock, Position


def storage(request):
    storages = Stock.objects.all()
    return render(request, 'storage.html', {'storages': storages, 'active': 'Склад'})

#
# def income(request, pk):
#     stock = Stock.objects.get(pk=pk)
#     PositionFormSet = modelformset_factory(Position, form=PositionForm)
