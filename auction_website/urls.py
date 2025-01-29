from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auction_home.urls')),# including the urls.py for the auction_home app
    path('', include('users.urls')),       # include the urls.py of the users app
    
]
