from django.shortcuts import render, get_object_or_404, redirect
from .models import Auction, Bid
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now
from django.core.paginator import Paginator
from .forms import AuctionForm

@login_required
def auctions(request):
    auction_list = Auction.objects.all().order_by('-created_at')  # Fetch all auctions, ordered by creation date
    paginator = Paginator(auction_list, 5)  # Show 5 auctions per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    auctions = paginator.get_page(page_number)  # Get the auctions for the current page
    return render(request, 'auctions.html', {'auctions': auctions})

@login_required
def my_auctions(request):
    user_auctions = Auction.objects.filter(created_by=request.user).order_by('-created_at')
    
    paginator = Paginator(user_auctions, 2)  # Show 2 auctions per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    user_auctions = paginator.get_page(page_number)  # Get the auctions for the current page
    
    return render(request, 'my_auctions.html', {'auctions': user_auctions})


@login_required
def edit_auction(request, pk):
    auction = get_object_or_404(Auction, pk=pk, created_by=request.user)  # Ensure the user owns the auction
    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES, instance=auction)
        if form.is_valid():
            form.save()
            return redirect('my_auctions')  # Redirect to "My Auctions" page after saving
    else:
        form = AuctionForm(instance=auction)  # Pre-fill the form with the auction's details
    return render(request, 'edit_auction.html', {'form': form, 'auction': auction})


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
        return redirect('auctions')  

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