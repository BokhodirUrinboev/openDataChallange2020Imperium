from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth import login, logout
from .forms import CreateUserForm

# Create your views here.


@unauthenticated_user
def sign_up_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('openDataChallange2020Imperium.viewer:login')


    else:
        form = CreateUserForm()
    return render(request, 'account/register.html', {'form': form})


@unauthenticated_user
def sign_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('openDataChallange2020Imperium.viewer:index')
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('openDataChallange2020Imperium.viewer:index')


def index(request):
    return render(request, 'index.html')