#from django.conf.url import url
from . import views
from django.conf.urls import url
urlpatterns=[
url(r'^$',views.index,name='index')
];