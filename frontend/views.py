from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models.users import *
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.


name = "The Alchemist Toolz"

METADATA = {
    'None': {
        'title':f'Home | {name}',
        'description':
            """
            The Alchemist Toolz is an Information and Communication Technology driven firm, 
            intentional and passionate about training young people with technological skills 
            to provide solutions for their immediate environment and the world at large
            """,
    },
    'about': {
        'title':'',
        'description':'',
    },
    'contact': {
        'title':'',
        'description':'',
    },
}



BASE_TEMPLATE = 'toolz'

def index(request, pagename=None, id=None):
    context = METADATA.get(str(pagename), 'None')
    # context.update({"page_title":"The Alchemist Tools"})

    try:
        id = request.user.id
        if pagename==None or pagename=="index" and not (str(pagename).__contains__('.html')):
            return render(request, f'{BASE_TEMPLATE}/index.html', context=context)
        elif (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):
            context['user_id'] = id
            return render(request, f'{BASE_TEMPLATE}/{pagename}.html', context=context)
        else:
            context['user_id'] = id
            return render(request, f'error/404.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))