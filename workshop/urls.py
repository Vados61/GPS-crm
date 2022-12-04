from django.urls import path

from workshop.views import index, workshop, finish_order, unfinished_order

urlpatterns = [
    path('', index, name='home'),
    path('workshop', workshop, name='workshop'),
    path('order/finish/<int:pk>', finish_order, name='finish_order'),
    path('order/unfinished/<int:pk>', unfinished_order, name='unfinished_order'),
]
