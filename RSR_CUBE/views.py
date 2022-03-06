from django.shortcuts import render


def home(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')
