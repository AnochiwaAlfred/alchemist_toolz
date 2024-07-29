
from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="elixir"),
    path(f"add_elixir/", URLShorten.as_view(), name="add_elixir"),    
    path("u/<str:slugs>", urlRedirect, name="redirect"),
]
