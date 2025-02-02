from django.shortcuts import render, get_object_or_404, redirect
from .models import Auction, Bid
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now

@login_required
def auctions(request):
    auctions = Auction.objects.all()  
    return render(request, 'auctions.html', {'auctions': auctions})



@login_required
def add_auction(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        starting_price = request.POST['starting_price']
        ends_at = request.POST['ends_at']
        image = request.FILES.get('image')

        Auction.objects.create(
            title=title,
            description=description,
            starting_price=starting_price,
            current_price=starting_price,
            created_by=request.user,
            ends_at=ends_at,
            image=image
        )
        return redirect('auctions')  # Replace 'auctions' with the name of your auctions page URL

    return render(request, 'add_auction.html')



@login_required
def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    bids = auction.bids.all().order_by('-created_at') 

    if request.method == 'POST':

        bid_amount = request.POST.get('bid_amount')
        if bid_amount:
            bid_amount = float(bid_amount)
            if bid_amount > (auction.current_price or auction.starting_price):

                Bid.objects.create(
                    auction=auction,
                    bidder=request.user,
                    amount=bid_amount
                )

                auction.current_price = bid_amount
                auction.save()
                return HttpResponseRedirect(reverse('auction_detail', args=[pk]))
            else:

                return render(request, 'auction_detail.html', {
                    'auction': auction,
                    'bids': bids,
                    'error': 'Your bid must be higher than the current price.'
                })

    return render(request, 'auction_detail.html', {
        'auction': auction,
        'bids': bids
    })