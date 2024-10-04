from ninja import Schema, FileEx, UploadedFile
from typing import List
from datetime import date, datetime




class AuthUserRegistrationSchema(Schema):
    email:str=None
    username:str=None  
    first_name:str=None    
    last_name:str=None    


class AuthUserRetrievalSchema(Schema):
    id:int=None
    email:str=None
    username:str=None    
    first_name:str=None    
    last_name:str=None    
    is_online:bool=None
    last_online:datetime=None
    is_active:bool=None
    is_staff:bool=None
    is_superuser:bool=None
    
    
class UserLoginSchema(Schema):
    email: str=None
    password: str=None
    
    
    
  