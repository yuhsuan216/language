from django.conf.urls import url
from ccc import views
urlpatterns = [
 url(r'^$', views.ccc, name='ccc'),
]