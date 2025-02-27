from django.db import models
from django.contrib.auth.models import User
from auctions.models import Auction
from django.conf import settings


class ChatMessage(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
    
    class Meta:
        ordering = ['-timestamp']
    
    

    