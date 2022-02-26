from turtle import mode
from django.db import models
from authentication.models import User

# Create your models here.

class Token(models.Model):
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE) #any user
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE) # admin user
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE) # volunteer user
    # geo_location = 
    image = models.ImageField()
    message = models.TextField(max_length=200)
    is_done = models.BooleanField(default=False)
    raised_date = models.DateField()
    assigned_date = models.DateField()
    done_date = models.DateField()

