from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    list_display = TRANSLATE_DISPLAY