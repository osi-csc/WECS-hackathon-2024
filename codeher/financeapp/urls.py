# financeapp/urls.py

from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),  # This URL will be used for the registration page
]
