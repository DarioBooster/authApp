from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(models.Model):
    nom : models.CharField(max_length=50, blank=True, null=True) # type: ignore
    
