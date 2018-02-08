from django.conf.urls import url, include
from . import views


app_name = 'users'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/logout/$', views.logout, name='logout'),
    url(r'^registro/$', views.register, name='register'),
]
