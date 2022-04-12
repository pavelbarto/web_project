from django.db import models

# Create your models here.

from django.db import models

class Film(models.Model):
    nazov = models.CharField(max_length=200)
    rezia = models.CharField(max_length=180)

class Zanr(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    nazov_zanru = models.CharField(max_length=80)

