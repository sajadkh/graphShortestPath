from django.db import models


class Path(models.Model):
    graph = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.IntegerField()

    def __str__(self):
        return "{0}->{1}".format(self.source, self.destination)


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    alarm = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.name)
