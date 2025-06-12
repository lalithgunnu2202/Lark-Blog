from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('all_blogs/',views.all_blogs_view, name='all_blogs'),
]