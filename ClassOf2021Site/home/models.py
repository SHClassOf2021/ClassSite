from django.db import models

# Create your models here.

class Announcement(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title_text

    class Meta():
        verbose_name = 'Announcement'
