from django.urls import path

from storage.views import storage

urlpatterns = [
    path('', storage, name='storage'),
    # path('income/<int:pk>', income, name='income')
    ]
