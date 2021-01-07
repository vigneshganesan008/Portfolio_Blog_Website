from django.db import models
from django.db.models.fields import TextField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    discription = TextField()
    date = models.DateField()