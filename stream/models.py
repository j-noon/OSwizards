from django.db import models
from django.utils import timezone

class StreamSettings(models.Model):
    channel_login = models.CharField(max_length=50, help_text="Twitch channel login (lowercase)")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Twitch: {self.channel_login}"


class ScheduleItem(models.Model):
    STATUS_CHOICES = [
        ("AUTO", "Auto (time-based)"),
        ("CANCELLED", "Cancelled"),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    status_override = models.CharField(max_length=20, choices=STATUS_CHOICES, default="AUTO")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_at"]

    def __str__(self):
        return f"{self.title} ({self.start_at})"

    def computed_status(self, now=None):
        now = now or timezone.now()

        if self.status_override == "CANCELLED":
            return "cancelled"
        if self.end_at < now:
            return "past"
        if self.start_at <= now <= self.end_at:
            return "live"
        return "upcoming"
