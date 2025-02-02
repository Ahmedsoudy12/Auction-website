from django.urls import path
from . import views

urlpatterns = [
    path('', views.auctions, name='auctions'), 
    path('<int:pk>/', views.auction_detail, name='auction_detail'),
    path('add/', views.add_auction, name='add_auction'),
]