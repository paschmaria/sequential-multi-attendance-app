from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("create/booking/confirm/", views.ConfirmBookingView.as_view(), name="confirm"),
    path("create/booking/select-clinic/", views.SelectClinicView.as_view(), name="select_clinic"),
    path("create/booking/select-date/", views.SelectDateTimeView.as_view(), name="select_date"),
    path("create/booking/select-lga/", views.SelectLGAView.as_view(), name="select_lga"),
    path("create/booking/select-state/", views.SelectStateView.as_view(), name="select_state"),
    path("create/booking/user-assessment/", views.UserAssessmentView.as_view(), name="user_assessment"),
    path("create/booking/add-info/", views.UserInfoView.as_view(), name="add_info"),
]
