from rest_framework import routers
from django.conf.urls import include
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [
    path("cards/", include(("apps.cards.urls", "apps.cards"), namespace="cards")),
] + router.urls
