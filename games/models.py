from django.db import models

class GameSeries(models.Model):
    CAMPAIGN = "campaign"
    ONE_SHOT = "one_shot"

    SERIES_TYPE_CHOICES = [
        (CAMPAIGN, "Campaign"),
        (ONE_SHOT, "One-shot"),
    ]

    series_type = models.CharField(max_length=20, choices=SERIES_TYPE_CHOICES)
    title = models.CharField(max_length=200)  # e.g. "King of the Eternal"
    system = models.CharField(max_length=200, blank=True)  # e.g. "Pathfinder 2e"
    description = models.TextField(blank=True)  # optional intro text
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["series_type", "sort_order", "title"]

    def __str__(self):
        if self.system:
            return f"{self.title} ({self.system})"
        return self.title


class EpisodeRecap(models.Model):
    series = models.ForeignKey(GameSeries, on_delete=models.CASCADE, related_name="episodes")
    episode_number = models.PositiveIntegerField()  # 1,2,3...
    title = models.CharField(max_length=200, blank=True)  # optional: "The Tavern Incident"
    recap = models.TextField()
    aired_on = models.DateField(blank=True, null=True)  # optional
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["episode_number"]
        unique_together = ("series", "episode_number")

    def __str__(self):
        return f"{self.series.title} - Ep {self.episode_number}"
