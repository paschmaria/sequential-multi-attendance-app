from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Location(models.Model):
    """
    Base class for capturing location
    """

    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Schedule(models.Model):
    """
    Keeps track of availability schedules for all service providers
    """

    is_available = models.BooleanField(default=False)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.is_available


class ServiceProvider(Location):
    """
    Model for all type of service providers

    - Test Centers (Hospital)
    - Super Markets
    """

    name = models.CharField(max_length=254)
    desc = models.TextField(_("description"))
    phone = PhoneNumberField()
    email = models.EmailField(max_length=50)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', 'state', 'lga')

    def __str__(self):
        return self.name


class HealthStatus(models.Model):
    """
    Keeps track of the health status of the user
    """

    cough = models.BooleanField(default=False)
    cold = models.BooleanField(default=False)
    diarrhea = models.BooleanField(default=False)
    sore_throat = models.BooleanField(default=False)
    body_aches = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    difficult_breath = models.BooleanField(default=False)
    traveled = models.BooleanField(default=False)    
    infected_trip = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Health Status")

    def __str__(self):
        return self.result

    def result(self):
        return ""


class Booker(models.Model):
    """
    Details of the person created the booking
    """

    name = models.CharField(_("full name"), max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    health_status = models.ForeignKey(
                        HealthStatus,
                        on_delete=models.CASCADE,
                        blank=True,
                        null=True
                    )

    def __str__(self):
        return self.name


class Booking(Location):
    """
    Model for saving booking to the database
    """

    date = models.DateTimeField()
    service_provider = models.ForeignKey(
                    ServiceProvider,
                    on_delete=models.CASCADE
                )
    booker = models.ForeignKey(
                    Booker,
                    on_delete=models.CASCADE,
                    blank=True,
                    null=True
                )
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f"{self.service_provider} {self.date}"