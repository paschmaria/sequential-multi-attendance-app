from django.db import models


class ServiceProvider(models.Model):
    """
    Model for all type of service providers

    - Test Centers (Hospital)
    - Super Markets
    """

    name = models.CharField(max_length=225)



class Booking(models.Model):
    """
    Model for saving booking to the database
    """

    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    date = models.DateField()