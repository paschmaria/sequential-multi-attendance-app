from django.db import models


class Location(models.Model):
    """
    Base class for capturing location
    """

    state = models.CharField(
                    max_length=50,
                    blank=True,
                    null=True
                )
    lga = models.CharField(
                    max_length=50,
                    blank=True,
                    null=True
                )

    class Meta:
        abstract = True