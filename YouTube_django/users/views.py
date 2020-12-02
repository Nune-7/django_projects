from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,username=username,password=password)

            if not user is None:
                login(request,user)

            messages.add_message(request, messages.SUCCESS, "User is created successfully")
            messages.add_message(request, messages.SUCCESS, "User is login")

            return redirect("login")
        else:
            messages.add_message(request, messages.SUCCESS, "User is not created successfully")

    form = UserRegisterForm()
    return render(request, 'registration/user_register.html', {'form': form})


