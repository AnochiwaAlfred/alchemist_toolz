from django.contrib import admin
from .models import ElixirOfLinks

# Register your models here.


@admin.register(ElixirOfLinks)
class ElixirOfLinksAdmin(admin.ModelAdmin):
    pass