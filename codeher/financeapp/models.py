from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    userPassword = models.CharField(max_length=128)  # To store hashed password
    startDate = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)  # Add the last_login field
    
    # If you want to make the user active or inactive
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
