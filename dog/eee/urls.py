from django.conf.urls import url
from eee import views

urlpatterns = [
    url(r'^$', views.eee, name='eee'),
]