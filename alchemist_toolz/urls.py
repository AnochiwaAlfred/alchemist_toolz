"""
URL configuration for alchemist_toolz project.
"""

from django.contrib import admin
from django.urls import path, include
from apis.api import api
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings

VERSION = "v1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("frontend.urls")),
    # path('elixirs/', include("elixir_of_links.urls")),

    # API URLS
    path(f"api/{VERSION}/", api.urls),


    # STATIC URLS
    url(r'^media/(?P<path>.*)$', serve,  {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
