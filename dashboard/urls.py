from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'dashboard'

urlpatterns = [
    path("", views.DashboardView.as_view(), name="home"),
    path(
        "create-service-provider/",
        csrf_exempt(views.ServiceProviderView.as_view()),
        name="create_sp"
    ),
]
