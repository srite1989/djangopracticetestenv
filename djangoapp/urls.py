from pipes import Template
from re import template
from django.urls import path
from unicodedata import name
from .views import indexView,loginView,authView,broadcast_sms
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('',indexView,name='home'),
    path('login/',loginView,name='login'),
    path('signin/',authView,name='signin'),
    path('broadcast',broadcast_sms,name='bcast'),
]
