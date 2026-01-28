from django.shortcuts import render
from .models import Profile
from stream.context import get_stream_section_context


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

    # ✅ Build your normal context
    context = {
        "show_profile_banner": show_profile_banner,
    }

    # ✅ Merge in stream app context (twitch_live, schedule_rows, etc.)
    context.update(get_stream_section_context())

    return render(request, "core/home.html", context)


def login_page(request):
    return render(request, "core/login.html")
