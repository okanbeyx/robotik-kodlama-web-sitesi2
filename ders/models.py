from django.db import models


# Create your models here.
class Tanit(models.Model):
    title = models.CharField(max_length=150)
    title1 = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True, upload_to='tanit/', verbose_name='image')


class Card(models.Model):
    title = models.CharField(max_length=150)
    title1 = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True, upload_to='cards/', verbose_name='image')


class About(models.Model):

    def __str__(self):
        return self.title
