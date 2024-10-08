# financeapp/forms.py

from django import forms
from .models import User, Goals, Transactions, Budgets

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'userPassword']
    
    userPassword = forms.CharField(widget=forms.PasswordInput())  # To hide password input

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    userPassword = forms.CharField(widget=forms.PasswordInput())

class TransactionAddForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['TransactionType','Category','amount']

