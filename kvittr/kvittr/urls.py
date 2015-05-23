from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('theme.urls')),
    url(r'^useraccounts/', include('useraccounts.urls')),
    url(r'^posts/', include('posts.urls')),
]
