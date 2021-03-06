from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from Ressources.forms import RegisterForm

from .models import Citoyen, Role
# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error login, try again"))
            return redirect('members:login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Vous êtes déconnecté avec succes !'), {})
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            groupe = Group.objects.get(name='utilisateur')
            user.groups.add(groupe)
            #form = Citoyen(user=user, actif=True)
            #form.save()
            login(request, user)
            messages.success(request, ('Inscription réalisé avec succès'))
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'authenticate/register.html', {
        'form':form,
    })