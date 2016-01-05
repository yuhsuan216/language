from django.conf.urls import url
from aaa import views

urlpatterns = [
    url(r'^$', views.aaa, name='aaa'),
]