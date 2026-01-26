from django.shortcuts import render
from .models import Profile


def home(request):
    show_profile_banner = False

    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(
            user=request.user,
            defaults={"timezone": "Europe/London"},
        )

        # Profile completeness check
        show_profile_banner = not all([
            profile.display_name,
            profile.timezone,
            profile.contact_email,
            profile.avatar,
        ])

    return render(
        request,
        "core/home.html",
        {
            "show_profile_banner": show_profile_banner,
        },
    )


def login_page(request):
    return render(request, "core/login.html")
