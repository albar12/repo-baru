from django.conf.urls import url, include
from django.contrib import admin
from . import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cylops/', include('cylops.urls')),
    url(r'^hydra/', include('hydra.urls')),
    url(r'^minotaur/', include('minotaur.urls')),
    url(r'^cerberus/', include('cerberus.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^$', views.index),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
