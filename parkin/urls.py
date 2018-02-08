from django.conf.urls import url, include

from . import views

app_name = 'park'

urlpatterns = [
    url(r'^$', views.park, name='park'),
    url(r'^terminal/(?P<idt>\d+)/$', views.change_state, name='terminal'),
    url(r'^close/$', views.close, name='close'),
]
