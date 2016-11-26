from django.conf.urls import include, url
from rest_framework import routers

from main.views import StationViewSet, BusViewSet, LineViewSet

router = routers.DefaultRouter()
router.register(r'station', StationViewSet)
router.register(r'bus', BusViewSet)
router.register(r'line', LineViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
