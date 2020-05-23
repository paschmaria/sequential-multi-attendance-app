from django import forms
from django.utils.translation import ugettext_lazy as _

from dashboard.models import ServiceProvider

from .models import Booking
from .states import STATES_DATA as states


class StateForm(forms.Form):
    """
    Form for selecting User preferred booking state
    """

    STATE_CHOICES = [
        (state['state']['name'].lower(), state['state']['name']) for state in states
    ]

    state = forms.ChoiceField(choices=STATE_CHOICES,
                        initial=STATE_CHOICES[0][0],
                        error_messages={
                            'required': _('Kindly select a state')
                        })


class LGAForm(forms.Form):
    """
    Form for selecting User preferred booking LGA
    """
    
    def __init__(self, *args, **kwargs):
        self.lgas = kwargs.pop('lgas', []) # list of LGA for selected state is passed as a kwargs to form
        super().__init__(*args, **kwargs)
        choices = [(lga['name'].lower(), lga['name']) for lga in self.lgas]
        self.fields['lga'] = forms.ChoiceField(choices=choices,
                                            initial=choices[0][0],
                                            error_messages={
                                                'required': _('Kindly select a LGA')
                                            })


class DateTimeForm(forms.Form):
    """
    Form for selecting booking Date and time
    """

    date = forms.DateTimeField()


class ClinicForm(forms.Form):
    """
    Form for selecting Test center
    """

    def __init__(self, *args, **kwargs):
        self.clinics = kwargs.pop('clinics')
        super().__init__(*args, **kwargs)
        self.fields['date'] = forms.ChoiceField(choices=self.clinics)

    def clean(self):
        data = self.cleaned_data
        clinic = data.get('clinic')
        clinic = ServiceProvider.objects.get()
        data['clinic'] = clinic
        return data

