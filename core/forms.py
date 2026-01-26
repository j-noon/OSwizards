from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "display_name",
            "pronouns",
            "timezone",
            "bio",
            "contact_email",
            "avatar_url",
            "twitch_url",
            "youtube_url",
            "website_url",
        ]
        widgets = {
            "display_name": forms.TextInput(attrs={"placeholder": "Display name"}),
            "pronouns": forms.TextInput(attrs={"placeholder": "e.g. they/them"}),
            "timezone": forms.TextInput(attrs={"placeholder": "e.g. Europe/London"}),
            "bio": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us about you..."}),
            "contact_email": forms.EmailInput(attrs={"placeholder": "Email (optional)"}),
            "avatar_url": forms.URLInput(attrs={"placeholder": "Avatar URL (temporary)"}),
            "twitch_url": forms.URLInput(attrs={"placeholder": "Twitch link (optional)"}),
            "youtube_url": forms.URLInput(attrs={"placeholder": "YouTube link (optional)"}),
            "website_url": forms.URLInput(attrs={"placeholder": "Website link (optional)"}),
        }
