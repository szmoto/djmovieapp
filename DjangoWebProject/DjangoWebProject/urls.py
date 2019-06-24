"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views


admin.autodiscover()

urlpatterns = [

    url(r'^',include('movieapp.urls',namespace='movie')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
