from django.db import models
from tinymce.models import HTMLField


class City(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Event(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    name = models.CharField(max_length=200)
    description = HTMLField()
    time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             default=None)

    def __str__(self):
        return self.name
