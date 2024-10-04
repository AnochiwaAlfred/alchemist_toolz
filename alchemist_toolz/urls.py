"""
URL configuration for alchemist_toolz project.
"""

from django.contrib import admin
from django.urls import path, include
from apis.api import api

VERSION = "v1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("frontend.urls")),
    # path('elixirs/', include("elixir_of_links.urls")),

    # API URLS
    path(f"api/{VERSION}/", api.urls)
]
