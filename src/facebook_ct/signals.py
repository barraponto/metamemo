from django.db.models.signals import post_save
from django.dispatch import receiver
from purl import URL

from . import tasks


def from_facebook(url):
    return URL(url).host().endswith("facebook.com")


def from_facebook_cdn(url):
    return URL(url).host().endswith("fbcdn.net")


@receiver(post_save, sender="core.MemoSource")
def on_source_save(sender, instance, created, **kwargs):
    # only run on new facebook.com profile sources
    if not created or not from_facebook(instance.url):
        return

    tasks.get_facebook_data.delay(instance.pk)


@receiver(post_save, sender="core.MemoItem")
def on_item_save(sender, instance, created, **kwargs):
    # only run on new facebook.com items
    if not created or not from_facebook(instance.url):
        return

    tasks.get_facebook_media.delay(instance.pk)


@receiver(post_save, sender="core.MemoMedia")
def on_media_save(sender, instance, created, **kwargs):
    # only run on new fbcdn.net items
    if not created or not from_facebook_cdn(instance.url):
        return

    tasks.download_fbcdn_media.delay(instance.pk)
