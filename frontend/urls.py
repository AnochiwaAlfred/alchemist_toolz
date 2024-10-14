from django.urls import path, include
from django.conf import settings
from .views import *

app_name = 'frontend'
urlpatterns = []

try:
    urlpatterns += [
        # path('', views.index, name='index'),
        # path('<str:pagename>', views.index, name='index'),
        path(f"", LoginFunction.as_view(), name="login"),      
        path(f"dashboard/", Dashboard.as_view(), name="dashboard"),
        path(f"register/", RegisterFunction.as_view(), name="register"),
        path(f"logout/", logoutFunction, name="logout"),
        path(f"change_password/", ChangePasswordFunction.as_view(), name="change_password"),      
        path(f"update_profile_picture/", UpdateProfilePictureFunction.as_view(), name="update_profile_picture"),  
        path(f"yt_downloader/", YouTubeDownloaderFunction.as_view(), name="yt_downloader"),  


        # # dynamic pages
        path(f"dashboard/<str:pagename>/", pageRouter, name="pagerouter"),

        # # dynamic changelist object
        path(f"dashboard/<str:appname>/<str:modelname>/list", ChangeListFunction.as_view(), name="changelist"),
        path(f"dashboard/<str:appname>/<str:modelname>/create", ChangeFormFunction.as_view(), name="changeform"),
        path(f"dashboard/<str:appname>/<str:objectid>/<str:modelname>/change", UpdateFormFunction.as_view(), name="updateform"),
        path(f"dashboard/<str:appname>/<str:objectid>/<str:modelname>/delete", DeleteChangeListObject, name="delete"),

    ]
except Exception as e:
    urlpatterns += []