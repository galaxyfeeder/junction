"""junction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

import main
from main.views import LineDetailView, StationDisplayDynamicView, StationDisplayStaticView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/api')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('main.api')),
    url(r'^line/(?P<pk>\d+)/$', LineDetailView.as_view()),
    url(r'^station/(?P<pk>\d+)/static/$', StationDisplayStaticView.as_view()),
    url(r'^station/(?P<pk>\d+)/dynamic/$', StationDisplayDynamicView.as_view()),
    url(r'^stop/(?P<stop_id>\d+)/addpeople/$', main.views.add_view),
]
