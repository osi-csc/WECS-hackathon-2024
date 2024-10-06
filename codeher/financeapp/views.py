# financeapp/views.py

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to a login page after successful registration
    else:
        form = UserRegistrationForm()

    return render(request, 'financeapp/register.html', {'form': form})
