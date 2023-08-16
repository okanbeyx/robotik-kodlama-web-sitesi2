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

    def __str__(self):
        return self.title


class Yazi(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.text
