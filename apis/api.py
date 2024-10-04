from ninja import NinjaAPI
from ninja.security import django_auth, HttpBearer
from django.http import HttpResponseForbidden
from users.models import AuthUser
from decouple import config

from apis.v1.auth import router as auth_router
from apis.v1.os import router as os_router
from apis.v1.translate import router as translate_router

api = NinjaAPI(
    auth=None, 
    title="Alchemist Toolz", 
    description="This is an API with dynamic OpenAPI info section",
    # csrf=True
)


api.add_router("/auth/", auth_router)
api.add_router("/translate/", translate_router)


if config("ENVIRONMENT") == "development":
    api.add_router("/os/", os_router)