from django.shortcuts import render, redirect
from django.http.request import HttpRequest as HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages as django_message
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from typing import Any
from django.views.decorators.csrf import csrf_exempt
# from pytube import YouTube
# from pytube.download_helper import download_videos_from_channels, download_video, download_videos_from_list
# import pafy



from ..forms import *
from core.error_messages import ErrorMessages
from core.manifest import *
from core import languages
from users.models.users import *
from frontend.views.functions import PAGE_NOT_FOUND, custom_permission_required

# Create your views here.


name = "Alchemist Toolz"

BASE_DIR_NAME = "toolz"
APP_NAMESPACE = "frontend"
LOGIN_URL = f'/{BASE_DIR_NAME}/login'
LOGIN_NAMESPACE = f"{APP_NAMESPACE}:login"



# def index(request, pagename=None, id=None):
#     # context = METADATA.get(str(pagename), 'None')
#     # context.update({"page_title":"Alchemist Toolz"})

#     try:
#         id = request.user.id
#         if pagename==None or pagename=="index" and not (str(pagename).__contains__('.html')):
#             return render(request, f'{BASE_DIR_NAME}/index.html', context=context)
#         elif (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):
#             context['user_id'] = id
#             return render(request, f'{BASE_DIR_NAME}/{pagename}.html', context=context)
#         else:
#             context['user_id'] = id
#             return render(request, f'error/404.html', context=context)
#     except Exception as e:
#         return HttpResponse(str(e))



class Dashboard(TemplateView): 
    template_name = f"{BASE_DIR_NAME}/index.html"

    @method_decorator(login_required(login_url=reverse_lazy(LOGIN_NAMESPACE)))
    @method_decorator(custom_permission_required)
    def dispatch(self, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        # Add additional context data if needed
        context['page_title'] = name
        return context
    
class LoginFunction(TemplateView):
    template_name = f"{BASE_DIR_NAME}/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm
        context['LOGIN_TITLE'] = f"Welcome to {name}"
        context['page_title'] = f"{name} - Login"
        return context
    
    def post(self, request, *args, **kwargs):
        try:
            post_data = LoginForm(request.POST)
            if post_data.is_valid():
                username = post_data.cleaned_data.get('username')
                password = post_data.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user != None:
                    login(user=user, request=request)
                    user2 = AuthUser.objects.get(id=user.pk)
                    d =  AuthUser.objects.all()
                    user2.login()
                    request.session["user_id"] = user.pk
                    return redirect(f"{APP_NAMESPACE}:dashboard")
                else:
                    django_message.error(request, f"{ErrorMessages.FAILED_LOGIN_MESSAGE}")
                    return redirect(f"{APP_NAMESPACE}:login")
                    # return HttpResponseRedirect(redirect_to=LOGIN_URL)

            else:
                django_message.error(request, f"{ErrorMessages.FAILED_LOGIN_MESSAGE}")
                return redirect(f"{APP_NAMESPACE}:login")
                # return HttpResponseRedirect(redirect_to=LOGIN_URL)
        except Exception as e:
            return HttpResponse(e)
        


class RegisterFunction(TemplateView):
    template_name = f"{BASE_DIR_NAME}/register.html"
    
    @method_decorator(login_required(login_url=reverse_lazy(LOGIN_NAMESPACE)))
    @method_decorator(custom_permission_required)
    def dispatch(self, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(self.request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{name} - Register"
        context['company'] = COMPANY_DETAILS
        context['form'] = RegisterForm
        return context
    
    @method_decorator(custom_permission_required)
    def post(self, request, *args, **kwargs):
        try:
            post_data = RegisterForm(request.POST)
            if post_data.is_valid():
                username = post_data.cleaned_data.get('username')
                email = post_data.cleaned_data.get('email')
                first_name = post_data.cleaned_data.get('first_name')
                last_name = post_data.cleaned_data.get('last_name')
                password = "1234"
                
                userCheck = AuthUser.objects.filter(Q(username=username) | Q(email=email))
                if not userCheck.exists():
                    user = AuthUser.objects.create(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.set_password(password)
                    user.save()
                    request.session["user_id"] = user.pk
                    return HttpResponseRedirect(reverse(f"{APP_NAMESPACE}:dashboard"))
                else:
                    django_message.error(request, "Username or Email already in Use")
                    return HttpResponseRedirect(reverse(f"{APP_NAMESPACE}:register"))
            else:
                django_message.error(request, f"{ErrorMessages.PARAM_ERROR}")
                return HttpResponseRedirect(reverse(f"{APP_NAMESPACE}:register"))
        except Exception as e:
            import traceback; traceback.print_exc();
            return HttpResponse(e)
        


@login_required(login_url=reverse_lazy(LOGIN_NAMESPACE))
def logoutFunction(request): 
    user = request.user
    user.logout()
    logout(request)
    return redirect(f"{APP_NAMESPACE}:login")


class ChangePasswordFunction(TemplateView):
    template_name = f"{BASE_DIR_NAME}/change_password.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChangePasswordForm
        context['page_title'] = f"{name} - Change Password"
        return context
    
    @method_decorator(custom_permission_required)
    def post(self, request, *args, **kwargs):
        try:
            post_data = ChangePasswordForm(request.POST)
            if post_data.is_valid():
                username = request.user.username
                old_password = post_data.cleaned_data.get('old_password')
                password = post_data.cleaned_data.get('password')
                confirm_password = post_data.cleaned_data.get('confirm_password')
                user = authenticate(username=username, password=old_password)
                if user != None:
                    # login(user=user, request=request)
                    if password==confirm_password:
                        user.set_password(password)
                        user.save()
                        django_message.success(request, f"{ErrorMessages.PASSWORD_CHANGED_MESSAGE}")
                        return redirect(f"{APP_NAMESPACE}:dashboard")
                    else:
                        django_message.error(request, f"{ErrorMessages.PASSWORD_NOT_MATCH_MESSAGE}")
                        return redirect(f"{APP_NAMESPACE}:change_password")
                else:
                    django_message.error(request, f"{ErrorMessages.PARAM_ERROR}")
                    return redirect(f"{APP_NAMESPACE}:change_password")
            else:
                django_message.error(request, f"{ErrorMessages.PARAM_ERROR}")
                return redirect(f"{APP_NAMESPACE}:change_password")
        except Exception as e:
            return HttpResponse(e)


class UpdateProfilePictureFunction(TemplateView):
    template_name = f"{BASE_DIR_NAME}/update_image.html"
    
    @method_decorator(login_required(login_url=reverse_lazy(LOGIN_NAMESPACE)))
    @method_decorator(custom_permission_required)
    def dispatch(self, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(self.request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{name} - Update Profile Image"
        context['company'] = COMPANY_DETAILS
        return context
    
    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if image:
            try:
                user = AuthUser.objects.get(id=request.user.id)
                # Assuming you have a field on the users model to store the image
                user.image = image
                user.save()
                message = "You have successfully updated your profile picture "
                # notification = NotificationUser(user=user, message=message)
                # notification.save()
                django_message.success(request, "Picture Updated Successfully")
                return redirect(f"{APP_NAMESPACE}:update_profile_picture")
            except AuthUser.DoesNotExist:
                django_message.error(request, "User Not Found")
                return redirect(f"{APP_NAMESPACE}:update_profile_picture")
        else:
            django_message.error(request, "No Image Found")
            return redirect(f"{APP_NAMESPACE}:update_profile_picture")
        
@login_required(login_url=reverse_lazy(LOGIN_NAMESPACE))
@custom_permission_required
def pageRouter(request, pagename): 
    try:
        context = {}
        context['title'] = f"{pagename}".title()
        if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):
            context['user_id'] = id
            context['page_title'] = name
            context['languages'] = languages.LANGUAGES_DICT
            
            return render(request, f"{BASE_DIR_NAME}/{pagename}.html", context)
        else:
            django_message.error(request, f"{ErrorMessages.PARAM_ERROR}")
            return redirect(f"{APP_NAMESPACE}:dashboard")
    except Exception as e:
        print(str(e))
        return redirect(f"{APP_NAMESPACE}:dashboard")




class YouTubeDownloaderFunction(TemplateView):
    template_name = f"{BASE_DIR_NAME}/yt_downloader.html"
    
    @method_decorator(login_required(login_url=reverse_lazy(LOGIN_NAMESPACE)))
    @method_decorator(custom_permission_required)
    def dispatch(self, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().dispatch(self.request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{name} - YouTube Downloader"
        context['company'] = COMPANY_DETAILS
        return context
    
    def post(self, request, *args, **kwargs):
        # https://www.youtube.com/watch?v=heMBf1ESFtk
        url = request.POST.get("youtube_link")
        try:
            user = AuthUser.objects.get(id=request.user.id)
            # yt = pafy.new(url)
            # print(yt.streams)
            print("------------------------------------------------------------------------------------------------------------------------------")
            context = {"yt":"yt"}

            return redirect(f"{APP_NAMESPACE}:yt_downloader", context)
        except AuthUser.DoesNotExist:
            django_message.error(request, "User Not Found")
            return redirect(f"{APP_NAMESPACE}:yt_downloader")
        watch_html