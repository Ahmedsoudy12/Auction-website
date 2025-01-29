from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'), 
    
]