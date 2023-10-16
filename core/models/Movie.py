from django.db import models

from core.models.Studio import Studio
from core.models.Producer import Producer


class Movie(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
    year = models.IntegerField(blank=False, null=False)
    studios = models.ManyToManyField(Studio, related_name="movies")
    producers = models.ManyToManyField(Producer, related_name="movies")

    def __str__(self):
        return self.title
