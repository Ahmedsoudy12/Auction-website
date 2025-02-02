from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auction_home.urls')),# including the urls.py for the auction_home app
    path('users/', include('users.urls')),       # include the urls.py of the users app
    path('auctions/', include('auctions.urls')),   # include the urls.py of the auctions app
    path('payments/', include('payments.urls')),   # include the urls.py of the payments app
    path('notifications/', include('notifications.urls')),   # include the urls.py of the notifications app
    path('reviews/', include('reviews.urls')),        # include the urls.py of the reviews app
    path('analytics/', include('analytics.urls')),    # include the urls.py of the analytics app
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
