from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from ninja import Router, FormEx
from ninja.security import django_auth
from typing import List, Union, Any
from django.contrib.auth import logout as contrib_logout
from django.contrib.auth import authenticate, login
import uuid
from django.contrib import messages as django_message
# from googletrans import Translator



from translate import Translator
from apis.schema.translate import *
from plugins.hasher import hasherGenerator, decrypter
from transmutation_engine.models import *
from users.models.users import AuthUser
from core.error_messages import ErrorMessages


router = Router(tags=["Translate Endpoints"])


@router.post("create_translation", response=Union[TranslateRetrievalSchema, str])
def create_translation(request, user_id:int, data:TranslateRegistrationModelSchema=FormEx(...)):
    original_text = str(data.dict().get("original_text"))
    source_language = str(data.dict().get("source_language"))
    target_language = str(data.dict().get("target_language"))
    user = get_object_or_404(AuthUser, id=user_id)
    # translator = Translator()
    # translated_text = translator.translate(original_text, src='en', dest='fr')
    # print(translated_text.text)
    if user:
        try:
            translator = Translator(from_lang=source_language, to_lang=target_language)
            translated_text = translator.translate(original_text)
            translation = Translate(**data.dict())
            translation.translated_text = translated_text
            translation.user = user
            translation.save()
            return translation
        except:
            res = TranslateRetrievalSchema(
                id=uuid.uuid4(),
                original_text="",
                translated_text=f"{ErrorMessages.NO_INTERNET}",
                source_language="",  
                target_language="",
                user=user
            )
            return res
    else:
        return user

@router.get("get_all_translations", response=List[TranslateRetrievalSchema])
def get_all_translations(request):
    translations = Translate.objects.all()
    return translations


@router.get("/{translation_id}/get/", response=Union[TranslateRetrievalSchema, str])
def get_translation_by_id(request, translation_id:uuid.UUID):
    translation = get_object_or_404(Translate, id=translation_id)
    return translation


@router.delete("/{translation_id}/delete/", response=Union[TranslateRetrievalSchema, str])
def delete_translation(request, translation_id:uuid.UUID):
    translation = get_object_or_404(Translate, id=translation_id)
    if translation:
        translation.delete()
        return "Translation deleted successfully"
    else:
        return translation


# 3fa85f64-5717-4562-b3fc-2c963f66afa6
