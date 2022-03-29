from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=15,  unique=True)
    std = models.IntegerField(null=False, default=1)
    regnum = models.IntegerField(null=False, default=1)