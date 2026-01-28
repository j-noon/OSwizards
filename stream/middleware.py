from zoneinfo import ZoneInfo
from django.utils import timezone

DEFAULT_TZ = "Europe/London"


class UserTimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = DEFAULT_TZ

        user = getattr(request, "user", None)
        if user and user.is_authenticated:
            profile = getattr(user, "profile", None)  # change if your related name differs
            if profile and getattr(profile, "timezone", ""):
                tzname = profile.timezone

        try:
            timezone.activate(ZoneInfo(tzname))
        except Exception:
            timezone.activate(ZoneInfo(DEFAULT_TZ))

        return self.get_response(request)
