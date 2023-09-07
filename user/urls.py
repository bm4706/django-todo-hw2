from django.shortcuts import render, redirect, HttpResponse
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup),
]
