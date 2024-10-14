from users.models import *
from django import template

register = template.Library()


@register.simple_tag
def get_user(request):
    if request.user:
        user_id = request.user.id
        user = AuthUser.objects.filter(id=user_id)
        if user.exists():
            user1 = user[0]
            if user1.image:
                return user1
            return user1
        else:
            return ""

@register.simple_tag
def get_user_image(request):
    if request.user:
        user_id = request.user.id
        user = AuthUser.objects.filter(id=user_id)
        if user.exists():
            user1 = user[0]
            image_url = request.build_absolute_uri(user1.image.url) if user1.image else "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/1200px-User_icon_2.svg.png"
            return image_url
            return user1
        else:
            return ""
        
        
# @register.simple_tag
# def get_user_notifications(request):
#     if request.user:
#         user_id = request.user.id
#         staff = Staff.objects.filter(id=user_id)
#         if staff.exists():
#             staff1 = staff[0]
#             notifications = NotificationStaff.objects.filter(staff=staff1)
#             return notifications
#         else:
#             return []
        
