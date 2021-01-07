from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    image =  models.ImageField(upload_to = "portfolio/images")
    url = models.URLField(blank=True)