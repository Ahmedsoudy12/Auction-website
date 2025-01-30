from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# function-based view
def payments(request):
    return render(request, 'payments.html')