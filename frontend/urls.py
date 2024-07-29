from django.urls import path, include
from django.conf import settings
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pagename>', views.index, name='index'),
]