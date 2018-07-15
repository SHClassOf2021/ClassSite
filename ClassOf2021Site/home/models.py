from django.db import models

# Create your models here.

class Announcement_Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text

    class Meta():
        verbose_name = 'Announcement Title'

class Announcement_Body(models.Model):
    topic = models.ForeignKey(Announcement_Title, on_delete=models.CASCADE)
    body_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.body_text

    class Meta():
        verbose_name = 'Announcement Body'
        verbose_name_plural = 'Announcement Bodies'
