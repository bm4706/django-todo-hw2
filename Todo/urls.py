from django import views
from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create),
    path('receive/', views.receive, name='receive'),
]
