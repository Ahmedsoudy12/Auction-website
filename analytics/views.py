from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# function-based view
def analytics(request):
    return render(request, 'analytics.html')

