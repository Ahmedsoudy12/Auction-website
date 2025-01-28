from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('home/', views.home, name='home'),  # Map the /home/ URL to the home view
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup')
]