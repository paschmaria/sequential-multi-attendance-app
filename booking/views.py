from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class SelectStateView(TemplateView):
    template_name = 'booking/state.html'


class SelectLGAView(TemplateView):
    template_name = 'booking/lga.html'


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