from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ProfileForm


@login_required
def profile_page(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    return render(request, "core/profile.html", {"profile": profile, "form": form})


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    return redirect(reverse("core:profile"))
