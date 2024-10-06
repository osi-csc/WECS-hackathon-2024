from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)  # Maps to SERIAL in PostgreSQL
    username = models.CharField(max_length=40)
    userPassword = models.CharField(max_length=40)
    startDate = models.DateField(auto_now_add=True )

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
