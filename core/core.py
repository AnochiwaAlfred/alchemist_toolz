from django.db import models
import uuid
from django.utils import timezone
from core.core_attrs import CoreAttrs


class CoreBaseModel(models.Model, CoreAttrs):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp =  models.DateField(auto_created=True, default=timezone.now, editable=False)

    
    
    
    class Meta:
        abstract = True
