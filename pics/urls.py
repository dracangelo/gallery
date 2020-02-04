from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^search/$',views.search,name='search'),
    url(r'^locations/$',views.places,name='places'),
    url(r'^locations/somewhere/$',views.somewhere,name='somewhere'),
    url(r'^locations/nairobi$',views.nairobi,name='nairobi'),
    url(r'^locations/france$',views.france,name='france'),
    url(r'^locations/wild$',views.wild,name='wild'),
    url(r'^locations/mombasa$',views.mombasa,name='mombasa'),
    url(r'^locations/belgium$',views.belgium,name='belgium'),
    
   ]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)