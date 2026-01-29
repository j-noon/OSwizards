from datetime import timedelta, datetime, time
from django.http import JsonResponse
from django.utils import timezone
from .models import StreamSettings, ScheduleItem
from .services.twitch import is_channel_live


def twitch_status(request):
    settings_obj = StreamSettings.objects.filter(is_active=True).first()

    if not settings_obj:
        return JsonResponse({"live": False})

    try:
        live = is_channel_live(settings_obj.channel_login)
    except Exception:
        live = False

    return JsonResponse({"live": live})


def schedule_statuses(request):
    now = timezone.now()
    grace_start = now - timedelta(hours=24)

    today = timezone.localdate()
    end_day = today + timedelta(days=7)
    end_window = timezone.make_aware(datetime.combine(end_day, time.min))

    items = (
        ScheduleItem.objects
        .filter(start_at__lt=end_window, end_at__gte=grace_start)
        .only("id", "start_at", "end_at", "status_override")
    )

    payload = [{"id": it.id, "status": it.computed_status(now=now)} for it in items]
    return JsonResponse({"items": payload})
