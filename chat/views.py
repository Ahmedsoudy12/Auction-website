from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render
from auctions.models import Auction
from .models import ChatMessage

# function-based view

def chat(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    messages = ChatMessage.objects.filter(auction=auction).order_by('timestamp')

    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(auction=auction, user=request.user, message=message)

    return render(request, 'chat.html', {'auction': auction, 'messages': messages})