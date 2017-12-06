from django.db import models

class Movie(models.Model):
    popularity = models.DecimalField(max_digits=20, decimal_places=2)
    director = models.CharField(max_length = 128)
    imdb_score = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
