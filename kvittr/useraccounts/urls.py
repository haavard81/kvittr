from django.conf.urls import patterns, url
from useraccounts import views

urlpatterns = patterns('',
    url(r'^login$', views.user_login, name='user_login'),
    url(r'^logout$', views.user_logout, name='user_logout'),
    url(r'^register$', views.user_register, name='user_register'),
    url(r'^edit$', views.user_edit, name='user_edit'),
)