from zoneinfo import available_timezones
from .models import Profile
from .forms import ProfileForm


def profile_modal_context(request):
    if not request.user.is_authenticated:
        return {}

    profile, _ = Profile.objects.get_or_create(user=request.user)
    return {
        "profile_form": ProfileForm(instance=profile),
        "timezones": sorted(available_timezones()),
    }
