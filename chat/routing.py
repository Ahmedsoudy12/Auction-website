from django.urls import path
from . import consumers

print("WebSocket URL patterns loaded...")  # Debugging: Ensure this is printed

websocket_urlpatterns = [
    path('ws/chat/<int:auction_id>/', consumers.ChatConsumer.as_asgi()),
]