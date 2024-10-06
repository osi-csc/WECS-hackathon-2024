# financeapp/urls.py

from django.urls import path
from .views import register, user_login, home

urlpatterns = [
    path('', home, name='home'),  # Set home as the root URL
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),  # Add login URL
]
