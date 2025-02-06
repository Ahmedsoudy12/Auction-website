from django.urls import path
from . import views

urlpatterns = [
    path('', views.auctions, name='auctions'), 
    path('<int:pk>/', views.auction_detail, name='auction_detail'),
    path('add/', views.add_auction, name='add_auction'),
    path('my-auctions/', views.my_auctions, name='my_auctions'),
    path('edit-auction/<int:pk>/', views.edit_auction, name='edit_auction'),
]