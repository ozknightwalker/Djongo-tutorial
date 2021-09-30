from rest_framework import viewsets

from .models import Card
from .serializers import CardSerializer


class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
