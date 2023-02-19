"""Определение схемы URL для practicmetrology"""

from django.urls import path 
from . import views

app_name = 'practicmetrology'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]