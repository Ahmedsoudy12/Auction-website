from django.urls import path
from . import views  

urlpatterns = [
    path('<int:auction_id>/', views.chat, name='chat'),
    
]



