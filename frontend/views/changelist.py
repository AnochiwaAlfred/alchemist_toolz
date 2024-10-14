import importlib
from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages as django_message
from typing import List
from frontend.views.functions import PAGE_NOT_FOUND, custom_permission_required



BASE_DIR_NAME = "toolz/"
APP_NAMESPACE = "frontend"
LOGIN_URL = f'/{BASE_DIR_NAME}/'
LOGIN_NAMESPACE = f"{APP_NAMESPACE}:login"




class ChangeListFunction(TemplateView):
    """For change list """
    template_name = f"{BASE_DIR_NAME}/change_list.html"

    @method_decorator(login_required(login_url=reverse_lazy(LOGIN_NAMESPACE)))
    @method_decorator(custom_permission_required)
    def dispatch(self, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(self.request, *args, **kwargs)
    
    def import_by_name(self, appname, modelname):
        try:
            imported_module = importlib.import_module(f"{appname}.models")
            return imported_module
        except ImportError as e:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            userid = self.request.user.pk
            appname = kwargs.get("appname")
            modelname = kwargs.get("modelname")
            importedapp = self.import_by_name(appname, modelname)

            if hasattr(importedapp, modelname):
                obj = getattr(importedapp, modelname)
                object_list = obj.objects.all()
                context['object_list'] = object_list
                context['object'] = obj
                context['page_title'] = "Alchemist Toolz"
                context['action_title'] = str(modelname).upper()
            
        except Exception as e:
            return context
        return context
    