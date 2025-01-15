from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transakcja, CelOszczednosciowy, Powiadomienie

# Widok dla strony głównej
@login_required
def dashboard(request):
    return render(request, 'folder_aplikacji/base.html')

def logowanie(request):
    return render(request, 'folder_aplikacji/login.html')