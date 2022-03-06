from django.apps import AppConfig


class InstagramCtConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "instagram_ct"

    def ready(self):
        from . import signals  # noqa
