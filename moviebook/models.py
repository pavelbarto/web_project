from django.db import models

# Create your models here.

from django.db import models

class Film(models.Model):
    nazov = models.CharField(max_length=200)
    rezia = models.CharField(max_length=180)

    def __str__(self):
        return "Nazov: {0} | Rezia: {1}".format(self.nazov, self.rezia)

class Zanr(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    nazov_zanru = models.CharField(max_length=80)

    def __str__(self):
        return "Film: {0} | Nazov_zanru: {1}".format(self.film, self.nazov_zanru)

