from django.db.models.signals import post_save
from django.dispatch import receiver
from purl import URL

from .tasks import get_facebook_data


@receiver(post_save, sender="core.MemoSource")
def on_source_save(sender, instance, created, **kwargs):
    # only run on new facebook.com profile sources
    if not created or not URL(instance.url).host().endswith("facebook.com"):
        return

    try:
        username = URL(instance.url).path().split("/").pop(1)
    except IndexError:
        pass
    else:
        get_facebook_data.delay(username)
