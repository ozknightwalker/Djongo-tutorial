from django.core.asgi import get_asgi_application
# from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                # path("ws/$", consumers.AsyncChatConsumer.as_asgi()),
            ])
        )
    )
})
