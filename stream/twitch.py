import requests
from django.conf import settings
from django.core.cache import cache

TOKEN_KEY = "twitch_app_token"


def get_app_token():
    cached = cache.get(TOKEN_KEY)
    if cached:
        return cached

    r = requests.post(
        "https://id.twitch.tv/oauth2/token",
        params={
            "client_id": settings.TWITCH_CLIENT_ID,
            "client_secret": settings.TWITCH_CLIENT_SECRET,
            "grant_type": "client_credentials",
        },
        timeout=10,
    )
    r.raise_for_status()
    data = r.json()

    token = data["access_token"]
    expires = int(data.get("expires_in", 3600))
    cache.set(TOKEN_KEY, token, timeout=max(60, expires - 60))
    return token


def is_channel_live(channel_login: str) -> bool:
    if not settings.TWITCH_CLIENT_ID or not settings.TWITCH_CLIENT_SECRET:
        return False

    token = get_app_token()
    headers = {
        "Client-Id": settings.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    r = requests.get(
        "https://api.twitch.tv/helix/streams",
        headers=headers,
        params={"user_login": channel_login},
        timeout=10,
    )
    r.raise_for_status()
    return bool(r.json().get("data"))
