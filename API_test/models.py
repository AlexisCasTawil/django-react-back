from django.db import models

# Create your models here.

# class comp(models.Model):
#   name = models.CharField(max_length=50)
#   email = models.CharField(max_length=50)
#   website = models.CharField(max_length=80)
#   fundator = models.CharField(max_length=60)
  
class games(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=30)
  website = models.CharField(max_length=80)
  company = models.CharField(max_length=60)
  