from django.urls import path

from . import views


urlpatterns = [
    path("bot/", views.whatsapp_bot, name="whatsapp_bot")
]
