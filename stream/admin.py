from django.contrib import admin
from .models import StreamSettings, ScheduleItem


@admin.register(StreamSettings)
class StreamSettingsAdmin(admin.ModelAdmin):
    list_display = ("channel_login", "is_active")
    list_editable = ("is_active",)


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ("title", "start_at", "end_at", "status_override", "updated_at")
    list_filter = ("status_override",)
    search_fields = ("title", "description")
