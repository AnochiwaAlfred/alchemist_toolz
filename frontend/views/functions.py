from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from functools import wraps

from users.models import AuthUser

PAGE_NOT_FOUND = "frontend/404.html"
BASE_DIR_NAME = "frontend"
LOGIN_URL = f'/{BASE_DIR_NAME}/login'


def custom_permission_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_id = request.user.id
        user = AuthUser.objects.filter(id=user_id)
        if not user.exists():
            return render(request=request, template_name=PAGE_NOT_FOUND, status=404, context={"redirect_url":LOGIN_URL, 'content':"Login"})
        elif not isinstance(user[0], AuthUser):
            return render(request=request, template_name=PAGE_NOT_FOUND, status=404, context={"redirect_url":LOGIN_URL, 'content':"Login"})
        return view_func(request, *args, **kwargs)
    return wrapper

