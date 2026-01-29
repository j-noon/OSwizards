from django.shortcuts import render
from .models import GameSeries


def games(request):
    series_qs = GameSeries.objects.filter(is_published=True).prefetch_related("episodes")

    campaigns = [s for s in series_qs if s.series_type == GameSeries.CAMPAIGN]
    one_shots = [s for s in series_qs if s.series_type == GameSeries.ONE_SHOT]

    context = {
        "campaigns": campaigns,
        "one_shots": one_shots,
    }
    return render(request, "games/games.html", context)
