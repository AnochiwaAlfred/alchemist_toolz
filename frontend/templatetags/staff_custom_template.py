# import importlib
# from django import template
# from django.template.loader import render_to_string
# from appcore.models import Plugins
# from django.contrib.auth.decorators import permission_required
# from functools import reduce
# import operator
# import traceback

# register = template.Library()


# @register.simple_tag
# def plugin(request=None, plugin_type="", context={}):
#     try:
#         context = context
#         pl = Plugins.objects.all().filter(plugin_type=plugin_type, status=True)
#         if pl.exists():
#             found = pl.first()
#             templated = render_to_string(
#                             template_name=f"{found.template_file}", 
#                             context=context, 
#                             request=request
#                         )
#             return templated
#         else:
#             return ""
#     except Exception as e:
#         return str(e)



# @register.simple_tag
# def template_loader(request=None, path='', context={}):
#     try:
#         context = context
#         templated = render_to_string(template_name=path, context=context, request=request)
#         return templated
#     except Exception as e:
#         return str(e)


# @register.simple_tag
# def show_count(object, **kwargs):
#     '''
#         Using the importlib to import relative object path.
#         this will have some filter arguments from kwargs.
#     '''
#     try:
#         module_name, class_name = object.rsplit('.', 1)
#         module = importlib.import_module(module_name)
#         app_obj = getattr(module, class_name)
        
#         if len(kwargs) > 0:
#             app = app_obj.objects.all().filter(**kwargs)
#             return app.count()
#         else:
#             return app_obj.objects.all().count()
#     except Exception as e:
#         return f"{e}"
    

# @register.simple_tag
# def show_filtered_data(object=None, order_by='created', **kwargs):
#     if object == None:
#         return "Object can not be None."
#     try:
#         module_name, class_name = object.rsplit('.', 1)
#         module = importlib.import_module(module_name)
#         app_obj = getattr(module, class_name)
#         if len(kwargs) > 0:
#             app = app_obj.objects.all().filter(**kwargs).order_by(order_by)
#             return app
#     except Exception as e:
#         return f"{e}"



# @register.simple_tag
# def show_data_list(object=None, limit=6, order_by='created'):
#     try:
#         module_name, class_name = object.rsplit('.', 1)
#         module = importlib.import_module(module_name)
#         app_obj = getattr(module, class_name)
#         app = app_obj.objects.all().order_by(order_by)
#         app = app[:limit]
#         return app
#     except Exception as e:
#         return f"{e}"




# @register.inclusion_tag(
#                     filename="staff/change_list_tools.html", 
#                     takes_context=True,
#                     )
# def change_lists_tools(context, request=None, object=None, queryset=None ):
#     container = []
#     if hasattr(object, 'list_display'):
#         list_display = object.list_display(request)
#         verbose_name =  object._meta.verbose_name
#         query_set =  object.get_queryset(request=request, queryset=queryset)
        
      
#         # filter_list_display = [lst for lst in list_display if hasattr(object, lst)]
#         filter_list_display = [lst for lst in list_display]
#         context['filter_list_display'] = filter_list_display
#         context['queryset'] = query_set
#         context['verbose_name'] = verbose_name
#         context['list_display'] = [str(x).replace("_", " ") for x in list_display ]
#     return context

# @register.simple_tag
# def get_attribute(query, name):
#     try:
#         if hasattr(query, name):
#            data = getattr(query, name)
#            if callable(data):
#                return data()
#            else:
#                return data
#     except:
#         return ''

# @register.inclusion_tag(
#                     filename="staff/change_form_tools.html", 
#                     takes_context=True,
#                     )
# def change_form_tools(context, request=None, object=None ):
#     verbose_name =  object._meta.verbose_name
#     if hasattr(object, 'form'):
#         fm = getattr(object, 'form')
#         context['dataform'] = fm()
#         context['verbose_name'] = verbose_name
#     return context



# @register.inclusion_tag(
#                     filename="staff/update_change_form_tools.html", 
#                     takes_context=True,
#                     )
# def update_form_tools(context, request=None, object=None, model=None, objectid=None ):
#     if hasattr(object, 'form'):
#         fm = getattr(object, 'form')
#         m =  model.filter(id=objectid).get()
#         verbose_name =  object._meta.verbose_name
#         verbose_name_staff =  object.verbose_name_staff()
        
#         if objectid:
#             context['dataform'] = fm()(instance=m)
#         else:
#             context['dataform'] = fm()
#         context['verbose_name'] = verbose_name
#     return context 




# @register.simple_tag
# def show_total(number=0.00):
#     try: 
#         num = 0
#         num += number
#         return num
#     except Exception as e:
#         return str(e)
    


# @register.simple_tag
# def multiple(*args):
#     try:
#         container = [x for x in args if isinstance(x,int)]
#         result = reduce(operator.mul, container)
#         return result
#     except:
#         pass


# @register.simple_tag
# def multipleTwoOprands(oprand1, oprand2):
#     try:
#         result = oprand1 * oprand2
#         return result
#     except Exception as e:
#         return str(e)

# @register.filter
# def form_filter(form,size=4,group_size=3):
#     from django.utils.html import format_html,html_safe
#     container = [f for f in form ]
#     grouped_container = [container[i:i+group_size] for i in range(0, len(container), group_size)]
#     ht = ""
#     for form_object in grouped_container:
#         ht += "<div class='row'>"
#         for fm  in form_object:
#             ht += f"<div class='col-sm-{size}'>"
#             ht += f"<label>{fm.label}</label>"
#             ht += f"<div>{fm}</div>"
#             ht += "<div>"
#         ht += "</div>"
#     return format_html(ht)