from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)  # Maps to SERIAL in PostgreSQL
    username = models.CharField(max_length=40)
    userPassword = models.CharField(max_length=40)
    startDate = models.DateField(auto_now_add=True )

    def __str__(self):
        return self.username