from django.db import models


class SliderActiveChoice(models.IntegerChoices):
    ISACTIVE = 1, "Is Active"
    NOTACTIVE = 0, "Not Active"


class SliderShowOnlineChoice(models.IntegerChoices):
    SHOW = 1, "Show Slider"
    DONT_SHOW = 0, "Don't Show Slider"

class StatusChoice(models.TextChoices):
    VACANT = 'vacant', 'Vacant'
    OCCUPIED =  'occupied', 'Occupied'
    UNDER_CLEANING =  'under_cleaning', 'Under Cleaning'
    

    
class GenderChoice(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE =  'female', 'Female'