from django.conf.urls import url
from bbb import views

urlpatterns = [
    url(r'^$', views.bbb, name='bbb'),
]