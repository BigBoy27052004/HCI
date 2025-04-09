from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'myApp/dashboard.html')

def landing(request):
    return render(request, 'myApp/landing.html')

def login(request):
    return render(request, 'myApp/login.html')

def signup(request):
    return render(request, 'myApp/signup.html')

def forgotpassword(request):
    return render(request, 'myApp/forgotpassword.html')

def addtask(request):
    return render(request, 'myApp/addtask.html')
from django.shortcuts import render

def journal(request):
    return render(request, 'myApp/journal.html')

# Add other views similarly
