from django.conf.urls import url
from ddd import views

urlpatterns = [
    url(r'^$', views.ddd, name='ddd'),
]