# financeapp/forms.py

from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'userPassword']
    
    userPassword = forms.CharField(widget=forms.PasswordInput())  # To hide password input
