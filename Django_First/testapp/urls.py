from django.contrib import admin
from django.urls import path
from testapp.views import index

urlpatterns = [
    path('', index),
]