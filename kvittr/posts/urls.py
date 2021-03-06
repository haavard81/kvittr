from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.post_listing, name='post_listing'),
    url(r'^(\d+)/$', views.post_details, name='post_details'),
    url(r'^(\d+)/add_likes$', views.post_add_likes, name='post_add_likes'),         
)