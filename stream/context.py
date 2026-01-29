from datetime import timedelta, datetime, time
from django.utils import timezone
from .models import StreamSettings, ScheduleItem
from .services.twitch import is_channel_live


def get_stream_section_context():
    settings_obj = StreamSettings.objects.filter(is_active=True).first()

    twitch_live = False
    channel_login = None

    if settings_obj:
        channel_login = settings_obj.channel_login
        try:
            twitch_live = is_channel_live(channel_login)
        except Exception:
            twitch_live = False

    now = timezone.now()
    grace_start = now - timedelta(hours=24)

    # calendar cutoff: start of the day 7 days from today (exclusive)
    today = timezone.localdate()
    end_day = today + timedelta(days=7)
    end_window = timezone.make_aware(datetime.combine(end_day, time.min))

    items = (
        ScheduleItem.objects
        .filter(start_at__lt=end_window, end_at__gte=grace_start)
        .order_by("start_at")
    )
    schedule_rows = []
    for it in items:
        status = it.computed_status(now=now)
        schedule_rows.append({"item": it, "status": status})

    return {
        "twitch_live": twitch_live,
        "twitch_channel_login": channel_login or "oswizards",
        "schedule_rows": schedule_rows,
    }
