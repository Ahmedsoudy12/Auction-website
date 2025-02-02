from django.contrib import admin
from .models import Auction, Bid


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'starting_price', 'current_price', 'ends_at')  
    list_filter = ('created_at', 'ends_at')  
    search_fields = ('title', 'description')
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('auction', 'bidder', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('auction__title', 'bidder__username')
    
