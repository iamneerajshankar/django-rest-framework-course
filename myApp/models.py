from django.db import models

# Create your models here.


class MoviesLibraryModel(models.Model):
    name = models.CharField(verbose_name='Movie Name', help_text='Field for movie name',
                            blank=False, max_length=50)
    director = models.CharField(verbose_name='Director', help_text='Field for movie director',
                                blank=False, max_length=50)
    year = models.IntegerField(verbose_name='Year of Release', help_text='Field for movie release year',
                               blank=True)
    rating = models.DecimalField(verbose_name='IMDB Rating', help_text='Field for movie IMDB rating',
                                 blank=True, decimal_places=2, max_digits=6)
    franchise = models.CharField(verbose_name='Franchise', blank=True, max_length=50)

