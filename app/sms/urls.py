"""Sms urls endpoint for"""

from django.urls import path

from . import views


urlpatterns = [
    path('send-msg/', views.send_msg, name='send_msg'),
    path('new-msg/', views.notification, name='notification'),
]
