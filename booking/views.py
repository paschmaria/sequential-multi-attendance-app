from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import StateForm, LGAForm, DateTimeForm, ClinicForm
from .models import Booking
from .states import STATES_DATA
from .utils import get_clinics


class IndexView(TemplateView):
    template_name = 'index.html'


class SelectStateView(FormView):
    template_name = 'booking/state.html'
    form_class = StateForm

    def form_valid(self, form):
        state = form.cleaned_data.get('state')
        booking = Booking.objects.create(state=state)
        return HttpResponseRedirect(self.get_success_url(booking.uuid))

    def get_success_url(self, uuid):
        success_url = reverse_lazy('booking:select_lga',
                                kwargs={'pk': uuid})
        return str(success_url)


def select_lga(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return redirect(reverse('booking:select_state'))

    lgas = [i for j in STATES_DATA for i in j['state']['locals'] \
                if j['state']['name']==booking.state.title()]

    if request.method == 'POST':
        form = LGAForm(request.POST, lgas=lgas)

        if form.is_valid():
            lga = form.cleaned_data.get('lga')
            booking.lga = lga
            booking.save()
            return redirect(reverse('booking:select_date',
                                kwargs={'pk': booking.pk}))
    else:
        form = LGAForm(lgas=lgas)
    
    context = { 'form': form, }
    return render(request, 'booking/lga.html', context=context)


def select_date(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return redirect(reverse('booking:select_state'))

    if request.method == 'POST':
        form = LGAForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data.get('date')
            booking.date = date
            booking.save()
            return redirect(reverse('booking:select_clinic',
                                kwargs={'pk': booking.pk}))
    else:
        form = LGAForm()
    
    context = { 'form': form, }
    return render(request, 'booking/lga.html', context=context)


def choose_clinic(request, pk):
    try:
        booking = Booking.object.get(pk=pk)
    except Booking.DoesNotExist:
        return redirect(reverse('booking:select_state'))

    clinics = get_clinics(booking.pk)

    if request.method == 'POST':
        form = ClinicForm(request.POST, clinics=clinics)
        
        if form.is_valid():
            clinic = form.cleaned_data.get('clinic')
            booking.service_provider = clinic
            booking.save()
            return redirect(reverse('booking:user_info',
                                kwargs={'pk': booking.pk}))
    else:
        form = ClinicForm(clinics=clinics)

    context = { 'form': form }
    return render(request, 'booking/clinic.html', context=context)


# class SelectLGAView(FormView):
#     template_name = 'booking/lga.html'
#     form_class = LGAForm

#     def get(self, request, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             booking = Booking.objects.get(pk=pk)
#         except Booking.DoesNotExist:
#             return HttpResponseRedirect(reverse('booking:select_state'))

#         lgas = [i for j in STATES_DATA for i in j['state']['locals'] \
#                 if j['state']['name']==booking.state.title()]
#         context_data = self.get_context_data(lgas=lgas)
#         return self.render_to_response(context_data)

#     def get_context_data(self, **kwargs):
#         """Insert the form into the context dict."""
#         kwargs['form'] = self.get_form(kwargs['lgas'])
#         return super().get_context_data(**kwargs)

#     def get_form(self, lgas):
#         """Return an instance of the form to be used in this view."""
#         form_class = self.get_form_class()
#         return form_class(**self.get_form_kwargs(lgas))

#     def get_form_kwargs(self, lgas):
#         """
#         Return the keyword arguments for instantiating the form.
#         """
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'lgas': lgas})
#         return kwargs

#     def post(self, request, *args, **kwargs):
#         """
#         Handle POST requests: instantiate a form instance with the passed
#         POST variables and then check if it's valid.
#         """
#         print(kwargs)
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         lga = form.cleaned_data.get('lga')
#         # booking = Booking.objects.create(lga=lga)
#         return HttpResponseRedirect(self.get_success_url(booking.uuid))

#     def get_success_url(self, uuid):
#         success_url = reverse_lazy('booking:select_lga',
#                                 kwargs={'pk': uuid})
#         return str(success_url)


class SelectClinicView(TemplateView):
    template_name = 'booking/clinic.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SelectDateTimeView(TemplateView):
    template_name = 'booking/date.html'


class UserInfoView(TemplateView):
    template_name = 'booking/user_info.html'


class UserAssessmentView(TemplateView):
    template_name = 'booking/test.html'


class ConfirmBookingView(TemplateView):
    template_name = 'booking/confirm.html'