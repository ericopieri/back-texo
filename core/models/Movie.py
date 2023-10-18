from django.db import models

from core.models.Studio import Studio
from core.models.Producer import Producer


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    year = models.IntegerField(blank=False, null=False)
    winner = models.BooleanField(blank=False, null=False, default=False)
    studios = models.ManyToManyField(Studio, related_name="movies")
    producers = models.ManyToManyField(Producer, related_name="movies")

    def __str__(self):
        return self.title
