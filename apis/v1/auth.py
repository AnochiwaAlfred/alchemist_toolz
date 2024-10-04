from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from ninja import Router, FormEx
from ninja.security import django_auth
from typing import List, Union, Any
from django.contrib.auth import logout as contrib_logout
from django.contrib.auth import authenticate, login


from apis.schema.auth import *
from plugins.hasher import hasherGenerator, decrypter
from users.models.users import *



router = Router(tags=["Authentication"])


@router.post("/register-via-email/", auth=None)
def register_user_with_email(
    request,
    password: str,
    passwordConfirm: str,
    user_data: AuthUserRegistrationSchema = FormEx(...),
):
    if password==passwordConfirm:
        try:
            user = AuthUser.objects.create(**user_data.dict())
            user.set_password(password)
            user.save()
            return {"message": f"Registration successful. UserID:{user.id}"}
        except ValidationError:
            raise ValidationError('Username already exists.')
            # return str(e)
    else:
        raise ValidationError('Passwords do not match.')


    


@router.get("/{user_id}/get/", response=Union[AuthUserRetrievalSchema, str])
def get_user_by_id(request, user_id):
    user = get_object_or_404(AuthUser, id=user_id)
    return user


@router.get("/getAllUsers/", response=List[AuthUserRetrievalSchema])
def get_all_users(request):
    users = AuthUser.objects.all()
    return users


@router.delete("/deleteUser/{user_id}/")
def delete_user(request, user_id):
    user = AuthUser.objects.get(id=user_id)
    user.delete()
    return f"User {user.username} deleted successfully"


@router.post("/login")
def login_user(request, email: str, password: str):
    validate = AuthUser.objects.filter(email=email)
    if validate:
        validated = validate[0].username
        user = authenticate(request, username=validated, password=password)
        if user:
            login(request, user)
            hh = hasherGenerator()
            access_token = decrypter(**hh)
            user2 = AuthUser.objects.filter(id=user.id)[0]
            user2._set_token(access_token)
            # image_url = request.build_absolute_uri(user2.image.url) if user2.image else ""
            token=user2.token
            user2.login()
            return {
                "access_token": token, 
                "user_id":user.id, 
                "username":user2.username, 
                "email":user2.email, 
                # "image":image_url, 
                "message":'User Logged in Successfully'
            }
        else:
            return {"message": "Invalid Password"}
    else:
        return {"message": "Invalid Email"}



@router.post("/logout/{token}")
def logout(request, token):
    user = AuthUser.objects.filter(token=token)[0]
    user.logout()
    contrib_logout(request)
    user._clear_token()
    return {
        "message": "User Logged Out; You can sign in again using your username and password."
    }
