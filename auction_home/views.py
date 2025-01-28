from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render




# function-based view
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


# Create your views here.
