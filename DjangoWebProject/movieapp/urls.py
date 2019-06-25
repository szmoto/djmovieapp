
"""
Definition of urls for polls viewing and voting.
"""

from django.conf.urls import url

import movieapp.views

urlpatterns = [
    url(r'^$',
        movieapp.views.index,
        name='home'),
    url(r'^movie/(?P<pk>\d+)/$',
        movieapp.views.detail,
        name='detail'),
]
