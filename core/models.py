from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Core identity for your app (separate from Django username / Discord username)
    display_name = models.CharField(max_length=40, blank=True)

    # Optional extras
    pronouns = models.CharField(max_length=20, blank=True)   # e.g. "he/him", "she/her", "they/them"
    timezone = models.CharField(max_length=50, blank=True)   # store as text now; can validate later

    bio = models.TextField(max_length=300, blank=True)

    # Future commerce contact
    contact_email = models.EmailField(blank=True)

    # Socials (keep this tight and useful)
    twitch_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    # Phase 1 avatar storage: URL
    avatar = CloudinaryField("avatar", blank=True, null=True)

    # Currency placeholder
    currency = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Profile"
