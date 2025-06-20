from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.portolio_view, name='portfolio_view'),
    path('project/<int:proj_id>/',views.project_details_view, name='project_details_view'),
]
