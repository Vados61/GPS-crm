from django.urls import path

from workshop.views import index, workshop_view, order_view, client_view

urlpatterns = [
    path('', index, name='home'),
    path('workshop', workshop_view, name='workshop'),
    path('order', order_view, name='order'),
    path('order/<int:pk>', order_view),
    path('client', client_view, name='client'),
    path('client/<int:pk>', client_view),
]
