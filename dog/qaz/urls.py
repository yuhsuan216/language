from django.conf.urls import url
from qaz import views

urlpatterns = [
    url(r'^$', views.qaz, name='qaz'),
]