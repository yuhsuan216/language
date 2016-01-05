from django.conf.urls import url
from zxc import views

urlpatterns = [
    url(r'^$', views.zxc, name='zxc'),
    url(r'^category/(?P<categoryID>[0-9]+)/$', views.category, name='category'),
    url(r'^addCategory/$', views.addCategory, name='addCategory'),
    url(r'^addPage/(?P<categoryID>[0-9]+)/$', views.addPage, name='addPage'),
    url(r'^deleteCategory/(?P<categoryID>[0-9]+)/$', views.deleteCategory,name='deleteCategory'),
    url(r'^updateCategory/(?P<categoryID>[0-9]+)/$', views.updateCategory,name='updateCategory'),
    url(r'^updatePage/(?P<pageID>[0-9]+)/$', views.updatePage,name='updatePage'),
    url(r'^deletePage/(?P<pageID>[0-9]+)/$', views.deletePage,name='deletePage'),
]