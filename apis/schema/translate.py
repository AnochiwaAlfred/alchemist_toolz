from ninja import Schema, FileEx, UploadedFile, ModelSchema
from typing import List
from datetime import date, datetime
from apis.schema.auth import AuthUserRetrievalSchema
import uuid
from transmutation_engine.models import Translate




class TranslateRegistrationSchema(Schema):
    original_text:str=None
    source_language:str=None  
    target_language:str=None  


class TranslateRetrievalSchema(Schema):
    id:uuid.UUID=None
    original_text:str=None
    translated_text:str=None
    source_language:str=None  
    target_language:str=None
    user:AuthUserRetrievalSchema=None

    
class TranslateRegistrationModelSchema(ModelSchema):
    class Meta:
        model = Translate
        fields = ['original_text', 'source_language', 'target_language']
    
    
    
  