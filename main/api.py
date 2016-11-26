from django.conf.urls import include, url
from rest_framework import routers

from main.views import StationViewSet, BusViewSet

router = routers.DefaultRouter()
router.register(r'station', StationViewSet)
router.register(r'bus', BusViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
