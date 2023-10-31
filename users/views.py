from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Successfully Created, Login Now!")
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form':form})
