from django.db.models.signals import post_save
from django.dispatch import receiver
from purl import URL

from .tasks import get_facebook_data, get_facebook_media


def from_facebook(url):
    return URL(url).host().endswith("facebook.com")


@receiver(post_save, sender="core.MemoSource")
def on_source_save(sender, instance, created, **kwargs):
    # only run on new facebook.com profile sources
    if not created or not from_facebook(instance.url):
        return

    get_facebook_data.delay(instance.pk)


@receiver(post_save, sender="core.MemoItem")
def on_item_save(sender, instance, created, **kwargs):
    # only run on new facebook.com items
    if not created or not from_facebook(instance.url):
        return

    get_facebook_media.delay(instance.pk)
