from django.db.models.signals import post_save
from django.dispatch import receiver
from purl import URL

from . import tasks


def from_instagram(url):
    return URL(url).host().endswith("instagram.com")


def from_instagram_cdn(url):
    return URL(url).host().endswith("cdninstagram.com")


@receiver(post_save, sender="core.MemoSource")
def on_source_save(sender, instance, created, **kwargs):
    # only run on new facebook.com profile sources
    if not created or not from_instagram(instance.url):
        return

    tasks.get_instagram_data.delay(instance.pk)


@receiver(post_save, sender="core.MemoItem")
def on_item_save(sender, instance, created, **kwargs):
    # only run on new facebook.com items
    print(instance.url, from_instagram(instance.url))
    if not created or not from_instagram(instance.url):
        return

    tasks.get_instagram_media.delay(instance.pk)


@receiver(post_save, sender="core.MemoMedia")
def on_media_save(sender, instance, created, **kwargs):
    # only run on new fbcdn.net items
    if not created or not from_instagram_cdn(instance.url):
        return

    tasks.download_igcdn_media.delay(instance.pk)
