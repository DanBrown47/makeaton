from django.db import models
from authentication.models import User
from .utils import upload_image

# Create your models here.


class Token(models.Model):
    category = models.CharField(max_length=150, choices=(('Plastic', 'Plastic'), (
        'Bio-degradable', 'Bio-degradable'), ('Medical or Clinical Wastes', 'Medical or Clinical Wastes'), ('Industrial Sources of Wastes', 'Industrial Sources of Wastes'), ('Electronic sources of waste', 'Electronic sources of waste')))
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.DecimalField(
        max_digits=11, decimal_places=7, null=True, blank=True)
    lng = models.DecimalField(
        max_digits=11, decimal_places=7, null=True, blank=True)
    images = models.ImageField(upload_to=upload_image)
    message = models.TextField(max_length=200)
    number = models.TextField(max_length=14)
    is_done = models.BooleanField(default=False)
    raised_date = models.DateField(auto_now_add=True)
    done_date = models.DateField(null=True, blank=True)


class CatchToken(models.Model):
    catched_by = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
