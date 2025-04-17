from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/services.html')

def insurance(request):
    return render(request, 'core/insurance.html')

def contact(request):
    return render(request, 'core/contact.html')
