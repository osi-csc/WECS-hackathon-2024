from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password 
from .forms import UserRegistrationForm, UserLoginForm
from .models import User, Transactions, Goals, Budgets
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.userPassword = make_password(form.cleaned_data['userPassword'])  # Hash the password
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'financeapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['userPassword']
            user = User.objects.filter(username=username).first()  # Fetch the user

            if user and check_password(password, user.userPassword):  # Check hashed password
                request.session['user_id'] = user.userID  # Store user ID in session
                request.session['is_authenticated'] = True  # Custom flag for authentication
                messages.success(request, 'Login successful!')
                return redirect('home')  # Redirect to home/dashboard
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = UserLoginForm()

    return render(request, 'financeapp/login.html', {'form': form})

def user_logout(request):
    logout(request)  # Clears session
    request.session.flush()  # Remove all session data, including custom flags
    return redirect('home')  # Redirect to home after logout
    
def add_expense(request):
    expense = form.save(commit=False)
    transaction.transactionType = 
    transaction.categoryID=
    transaction.amount=
    transaction
    
def home(request):
    return render(request, 'financeapp/home.html')


