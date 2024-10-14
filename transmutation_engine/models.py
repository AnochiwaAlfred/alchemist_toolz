from django.db import models
from core.core import CoreBaseModel
from core.languages import LanguageChoice
from django.utils import timezone

# Create your models here.


TRANSLATE_DISPLAY = ["id", "original_text", "translated_text", "source_language", "target_language", "user", "timestamp"]

class Translate(CoreBaseModel):
    original_text = models.TextField(default="", blank=True)
    translated_text = models.TextField(default="", blank=True)
    source_language = models.CharField(max_length=50, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH, blank=True)
    target_language = models.CharField(max_length=50, choices=LanguageChoice.choices, default=LanguageChoice.FRENCH, blank=True)
    user = models.ForeignKey("users.AuthUser", on_delete=models.CASCADE, null=True, blank=True)
    timestamp =  models.DateTimeField(auto_created=True, default=timezone.now, editable=False)

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"

    def __str__(self):
        return f"{self.original_text} ({self.source_language} -> {self.target_language})"
    