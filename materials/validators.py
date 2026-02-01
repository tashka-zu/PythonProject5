from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def validate_video_link(value):
    if value:
        allowed_domains = ['youtube.com', 'www.youtube.com']
        parsed_url = urlparse(value)
        if parsed_url.netloc not in allowed_domains:
            raise ValidationError(f"Ссылка на видео должна быть только с YouTube. Ваша ссылка: {value}")
