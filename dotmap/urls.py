from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^data/(?P<datenumber>[0-9]+)/$', views.api, name='api'),
]
