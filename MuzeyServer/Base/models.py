from django.db import models


class Visitor(models.Model):
    UID = models.CharField(blank=False, max_length=10, default='')
    Name = models.CharField(blank=False, max_length=250, default='')
    Surname = models.CharField(blank=False, max_length=250, default='')
    Points = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.Name
