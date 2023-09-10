from django.urls import path
from .views import roommate
urlpatterns = [
    path('',roommate,name='roommate')
]
