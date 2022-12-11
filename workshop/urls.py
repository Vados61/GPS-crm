from django.urls import path

from workshop.views import index, workshop_view, order_view, client_view

urlpatterns = [
    path('', index, name='home'),
    path('workshop', workshop_view, name='workshop'),
    path('order/<int:order_pk>', order_view, name='order'),
    path('client', client_view, name='client'),
    path('client/<int:pk>', client_view),
]
