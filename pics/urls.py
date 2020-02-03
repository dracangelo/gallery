from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.landing,name='landing')
    url(r'^search/$',views.search,name='search'),


]