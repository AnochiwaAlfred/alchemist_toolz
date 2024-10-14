import importlib
from django.apps import apps
from django import template

from core.installed_apps import INSTALLEDAPPS
from transmutation_engine.models import Translate

register = template.Library()


@register.simple_tag
def get_model_objects(model_name="", id=None):
    try:
        PLACEHOLDER = []
        mods =  apps.get_models()
        for m in mods:
            model_name2 = m.__name__
            module = f"{m._meta.model.__module__}.{model_name2}"
            # print(model_name2)
            if model_name==model_name2:
                PLACEHOLDER.append(module)
                
        if len(PLACEHOLDER)>0:
            app = PLACEHOLDER[0]
            module_name, class_name = app.rsplit('.', 1)
            module = importlib.import_module(module_name)
            app_obj = getattr(module, class_name)
            objects = app_obj.objects.all()
            if id!=None:
                objects = app_obj.objects.filter(id=id)[0]
            return objects
        return []
    except Exception as e:
        return str(e)
    

@register.simple_tag
def get_user_translations(request):
    if request.user:
        user_id = request.user.id
        translations = Translate.objects.filter(user_id=user_id).order_by("timestamp").reverse()
        return translations
    
@register.simple_tag
def get_dict_item(d, key):
    value = d.get(key)
    return value