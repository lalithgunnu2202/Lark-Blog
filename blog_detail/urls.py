from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('blog/<int:blog_id>',views.blogdetail_view, name='blog_details')
]
