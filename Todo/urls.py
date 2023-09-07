from django.shortcuts import render, redirect, HttpResponse
from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create),
    path('read/<int:todo_id>/', views.read),  # 무슨 글을썼는지 보여주기 위함
    path('receive/', views.receive, name='receive'),
]
