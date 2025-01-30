from django.db import models

class AuctionAnalytics(models.Model):
    auction = models.ForeignKey('auctions.Auction', on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    bids = models.IntegerField(default=0)