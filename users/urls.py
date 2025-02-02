from django.urls import path
from . import views  # Import views from the current app


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'), 
    path('profile/', views.profile, name='profile'),
    
    
]


