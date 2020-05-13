from django.db import models


class Location(models.Model):
    """
    Base class for capturing location
    """

    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)

    class Meta:
        abstract = True