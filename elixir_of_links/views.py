import random
import string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.shortcuts import render

from elixir_of_links.models import ElixirOfLinks
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages as django_message
from django.views import View
from core.error_messages import ErrorMessages
from django.views.generic import TemplateView


BASE_DIR_NAME = "elixir"
APP_NAMESPACE = "elixir"
LOGIN_URL = f'/{BASE_DIR_NAME}/login'
LOGIN_NAMESPACE = f"{APP_NAMESPACE}:login"


# Create your views here.

def index(request):
    return HttpResponse("Welcome to Alchemist Toolz!")


class URLShorten(TemplateView):
    template_name = f"{BASE_DIR_NAME}.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = URLForm
        context['page_title'] = "Alchemist Tools - Elixir of Links"
        return context
    
    def post(self, request, *args, **kwargs):
        try:
            post_data = URLForm(request.POST)
            if post_data.is_valid():
                slug = ''.join(random.choice(string.ascii_letters))
                for x in range(10):
                    url = post_data.cleaned_data["url"]
                    new_url = ElixirOfLinks(url=url, slug=slug)
                    new_url.save()
            else:
                django_message.error(request, f"{ErrorMessages.FAILED_LOGIN_MESSAGE}")
                return HttpResponseRedirect(redirect_to=LOGIN_URL)
        except Exception as e:
            return HttpResponse(e)
        

def urlRedirect(request, slugs):
    data = ElixirOfLinks.objects.filter(slug=slugs).first()
    return redirect(data.url)