from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from common.models import Location


class Category(models.Model):
    """
    Categories of service providers
    """

    CATEGORIES = (
        ('test_center', 'Test Center'),
        ('supermarket', 'Supermarket'),
    )

    type = models.CharField(
                _("category type"),
                max_length=50,
                choices=CATEGORIES,
                default="test_center"
            )

    def __str__(self):
        return self.type


class ServiceProvider(Location):
    """
    Model for all categories of service providers

    - Test Centers (Hospital)
    - Super Markets
    """

    name = models.CharField(max_length=254)
    desc = models.TextField(_("description"))
    phone = PhoneNumberField()
    email = models.EmailField(max_length=50)

    class Meta:
        ordering = ('name', 'state', 'lga')

    def __str__(self):
        return self.name