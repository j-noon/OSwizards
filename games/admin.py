from django.contrib import admin
from .models import GameSeries, EpisodeRecap


class EpisodeRecapInline(admin.TabularInline):
    model = EpisodeRecap
    extra = 1
    fields = ("episode_number", "title", "recap", "aired_on", "is_published")
    ordering = ("episode_number",)


@admin.register(GameSeries)
class GameSeriesAdmin(admin.ModelAdmin):
    list_display = ("title", "series_type", "system", "is_published", "sort_order")
    list_filter = ("series_type", "is_published")
    search_fields = ("title", "system")
    list_editable = ("is_published", "sort_order")
    inlines = [EpisodeRecapInline]
