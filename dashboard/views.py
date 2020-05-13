from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView

from .forms import ServiceProviderForm
from .mixins import AjaxResponseMixin, JSONResponseMixin
from .models import ServiceProvider


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'


class ServiceProviderView(JSONResponseMixin, AjaxResponseMixin, CreateView):
    form_class = ServiceProviderForm
    model = ServiceProvider

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
