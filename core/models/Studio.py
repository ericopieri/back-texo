from django.db import models


class Studio(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, primary_key=True)

    def __str__(self):
        return self.name
