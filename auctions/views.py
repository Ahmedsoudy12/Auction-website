from django.shortcuts import render

def auctions(request):
    return render(request, 'auctions.html')
