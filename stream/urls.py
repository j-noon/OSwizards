from django.urls import path
from .views import twitch_status, schedule_statuses

urlpatterns = [
    path("twitch-status/", twitch_status, name="twitch_status"),
    path("schedule-statuses/", schedule_statuses, name="schedule_statuses"),
]
