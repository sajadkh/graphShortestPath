from django.db import models

# Create your models here.


class Source(models.Model):
    source = models.CharField(max_length=100)


class Path(models.Model):
    graph = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.IntegerField()

    def __str__(self):
        return "{0}->{1}".format(self.source, self.destination)
