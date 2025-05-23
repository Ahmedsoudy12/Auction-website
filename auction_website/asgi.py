"""
ASGI config for auction_website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns  # Import your WebSocket routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_website.settings')

print("Loading WebSocket routing...")  # Debugging: Ensure this is printed

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP requests
    "websocket": AuthMiddlewareStack(  # WebSocket requests
        URLRouter(
            websocket_urlpatterns
        )
    ),
})