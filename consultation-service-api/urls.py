from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register, redirectto, history, homeassist, allcases, casetag, updatecase

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^redirect/', redirectto, name = 'redirectto'),
    url(r'^history/', history),
    url(r'^homeassist/',homeassist),
    url(r'^allcases/',allcases),
    url(r'^casetag/(?P<pk>\w+)/$',casetag),
    url(r'^update/(?P<pk>\w+)/$',updatecase),
]