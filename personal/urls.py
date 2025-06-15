from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.dashboard_view, name='personal_dashboard'),
    path('journals/',views.journals_view, name='journal_dashboard'),
    path('creating/',views.add_journal, name='add_journal'),
    path('delete/<int:id>',views.delete_journal, name='delete_journal'),
    path('view_journal/<int:id>',views.view_journal, name='view_journal'),
]
