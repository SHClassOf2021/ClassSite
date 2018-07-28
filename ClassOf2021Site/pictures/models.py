from django.db import models

# Create your models here.

class FlickrAlbums(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=10000)

    class Meta():
        verbose_name = 'Photo Album'
        verbose_name_plural = 'Photo Albums'

    def __str__(self):
        return self.name
