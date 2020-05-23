from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("booking/create/add-info/<uuid:pk>/", views.UserInfoView.as_view(), name="add_info"),
    path("booking/create/confirm/<uuid:pk>/", views.ConfirmBookingView.as_view(), name="confirm"),
    path("booking/create/select-clinic/<uuid:pk>/", views.SelectClinicView.as_view(), name="select_clinic"),
    path("booking/create/select-date/<uuid:pk>/", views.SelectDateTimeView.as_view(), name="select_date"),
    path("booking/create/select-lga/<uuid:pk>/", views.select_lga, name="select_lga"),
    path("booking/create/select-state/", views.SelectStateView.as_view(), name="select_state"),
    path("booking/create/user-assessment/<uuid:pk>/", views.UserAssessmentView.as_view(), name="user_assessment"),
]
