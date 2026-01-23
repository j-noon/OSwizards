from django.urls import path
from . import views


app_name = "merchandise"

urlpatterns = [
    path("", views.merch, name="merch"),
]
