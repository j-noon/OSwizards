from django import forms
from django.core.exceptions import ValidationError
from zoneinfo import available_timezones

from .models import Profile


class ProfileForm(forms.ModelForm):
    timezone = forms.ChoiceField(choices=[], required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = [
            "display_name",
            "pronouns",
            "timezone",
            "bio",
            "contact_email",
            "avatar",
            "twitch_url",
            "youtube_url",
            "website_url",
        ]
        widgets = {
            "display_name": forms.TextInput(attrs={"placeholder": "Display name"}),
            "pronouns": forms.TextInput(attrs={"placeholder": "e.g. they/them"}),
            "bio": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us about you..."}),
            "contact_email": forms.EmailInput(attrs={"placeholder": "Email (optional)"}),
            "twitch_url": forms.URLInput(attrs={"placeholder": "Twitch link (optional)"}),
            "youtube_url": forms.URLInput(attrs={"placeholder": "YouTube link (optional)"}),
            "website_url": forms.URLInput(attrs={"placeholder": "Website link (optional)"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tz_list = sorted(available_timezones())
        self.fields["timezone"].choices = [("", "Select your timezone…")] + [
            (tz, tz) for tz in tz_list
        ]

    def clean_contact_email(self):
        email = self.cleaned_data.get("contact_email", "")
        # EmailField already validates properly if non-empty, so this is just a nicer message.
        if email and "@" not in email:
            raise ValidationError("Please enter a valid email address.")
        return email

    def clean_avatar(self):
        """
        Supports both normal Django uploads and Cloudinary-stored values.
        Only validate when a NEW file is uploaded (i.e., avatar is present in self.files).
        """
        img = self.cleaned_data.get("avatar")

        # Nothing provided
        if not img:
            return img

        # If the user didn't upload a new file, don't validate the existing stored value.
        # (CloudinaryResource can appear here and doesn't have .name/.content_type like UploadedFile.)
        if "avatar" not in getattr(self, "files", {}):
            return img

        # Content type validation (UploadedFile typically has content_type)
        content_type = getattr(img, "content_type", "") or ""
        allowed_types = {"image/jpeg", "image/png", "image/webp"}
        if content_type and content_type not in allowed_types:
            raise ValidationError("Avatar must be a PNG, JPEG, or WEBP image.")

        # Extension validation (safe even if .name is missing)
        filename = (getattr(img, "name", "") or "").lower()
        if filename and not filename.endswith((".png", ".jpg", ".jpeg", ".webp")):
            raise ValidationError("Avatar must be a PNG, JPG, or WEBP file.")

        # Optional: size limit (helps performance + avoids huge uploads)
        max_size = 5 * 1024 * 1024  # 5MB
        size = getattr(img, "size", None)
        if size and size > max_size:
            raise ValidationError("Avatar is too large (max 5MB).")

        return img
