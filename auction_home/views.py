from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# function-based view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

