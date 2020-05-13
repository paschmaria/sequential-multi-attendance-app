from django import forms
from django.forms.models import inlineformset_factory

from .models import Category, ServiceProvider


class ServiceProviderForm(forms.ModelForm):
    """
    Form for creating Service Providers
    """

    class Meta:
        model = ServiceProvider
        fields = (
            'name',
            'desc',
            'phone',
            'email',
            'state',
            'lga',
        )


# ServiceProviderFormset = inlineformset_factory(Category, ServiceProvider, ServiceProviderForm)
