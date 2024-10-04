from django.db import models
from core.core import CoreBaseModel

# Create your models here.

class ElixirOfLinks(CoreBaseModel):
    url = models.CharField(max_length=500)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return f"Short URL for {self.url} is {self.slug}"