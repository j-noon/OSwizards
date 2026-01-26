from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from zoneinfo import available_timezones

from .forms import ProfileForm
from .models import Profile


@login_required
def profile_page(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={"timezone": "Europe/London"},
    )
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    return render(
        request,
        "core/profile.html",
        {
            "profile": profile,
            "form": form,
            "timezones": sorted(available_timezones()),
        },
    )


@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={"timezone": "Europe/London"},
    )

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.setup_completed = True
            profile.save()
            return redirect(reverse("core:profile"))

        return render(
            request,
            "core/profile.html",
            {
                "profile": profile,
                "form": form,
                "timezones": sorted(available_timezones()),
            },
        )

    return redirect(reverse("core:profile"))
