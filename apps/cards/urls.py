from rest_framework import routers

from .views import CardsViewSet


router = routers.SimpleRouter()
router.register(r'', CardsViewSet)

urlpatterns = [] + router.urls
