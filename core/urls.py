from django.urls import path
from . import views_profile
from . import views


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_page, name="login_page"),
    path("profile/", views_profile.profile_page, name="profile"),
    path("profile/edit/", views_profile.profile_edit, name="profile_edit"),
]
