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

class TransactionTypes(models.Model): 
    transactionTypeID = models.AutoField(primary_key=True)
    transactionTypeName = models.CharField(max_length=70)
    
class Categories (models.Model):
    categoryID = model.AutoField(primary_key=true)
    categoryName = models.CharField(max_length=50)
    
class Transactions(models.Model):
    transactionID =models.AutoField(primary_key=True)
    transactionType= models.transactionType()#foriegn key to TransactionTypeName from TransactionTypes

class   
    def __str__(self):
        return self.username
