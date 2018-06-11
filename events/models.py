from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location


class Event(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 default=None)

    def __str__(self):
        return self.title
