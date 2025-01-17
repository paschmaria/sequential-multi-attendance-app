from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.models import Location
from dashboard.models import ServiceProvider


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


class Schedule(models.Model):
    """
    Keeps track of availability schedules for all service providers
    """

    is_available = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.is_available


class Booking(Location):
    """
    Model for saving booking to the database
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    schedule = models.ForeignKey(
                    Schedule,
                    on_delete=models.CASCADE,
                    blank=True,
                    null=True
                )
    service_provider = models.ForeignKey(
                    ServiceProvider,
                    on_delete=models.CASCADE,
                    blank=True,
                    null=True
                )
    booker = models.ForeignKey(
                    Booker,
                    on_delete=models.CASCADE,
                    blank=True,
                    null=True
                )
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ('schedule',)

    def __str__(self):
        return f"{self.service_provider} {self.schedule.start_time}"