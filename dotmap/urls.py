from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.mainboard, name='mainboard'),
    url(r'^api/(?P<datenumber>[0-9]+)$', views.api, name='api'),
]