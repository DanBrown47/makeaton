from django.db import models
from authentication.models import User
from .utils import upload_image

# Create your models here.

class Token(models.Model):
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE) #any user
    # assigned_by = models.ForeignKey(User, on_delete=models.CASCADE) # admin user
    # assigned_to = models.ForeignKey(User, on_delete=models.CASCADE) # volunteer user
    lat = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    lng = models.DecimalField(max_digits=11, decimal_places=7,null=True,blank=True)
    images = models.ImageField(upload_to=upload_image)
    message = models.TextField(max_length=200)
    is_done = models.BooleanField(default=False)
    raised_date = models.DateField(null=True,blank=True)
    assigned_date = models.DateField(null=True,blank=True)
    done_date = models.DateField(null=True,blank=True)

