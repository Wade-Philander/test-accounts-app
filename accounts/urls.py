from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('',views.home),
    path('products/',views.products),
    path('customers/',views.customers),
]
