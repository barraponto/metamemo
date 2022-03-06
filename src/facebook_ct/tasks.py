from celery import shared_task
from purl import URL
from django.db.utils import DataError
from core.models import MemoItem, MemoMedia, MemoSource
from .api import CrowdTangleAPI


@shared_task
def get_facebook_data(source_id):
    source = MemoSource.objects.get(pk=source_id)
    username = URL(source.url).path().split("/").pop(1)
    for post in CrowdTangleAPI(username):
        item = MemoItem(
            url=post["postUrl"], created=post["date"], raw=post, source=source
        )
        item.save()


facebook_media_types = {
    "video": MemoMedia.MediaTypes.VIDEO,
    "photo": MemoMedia.MediaTypes.IMAGE,
}


@shared_task
def get_facebook_media(item_id):
    item = MemoItem.objects.get(pk=item_id)
    for media in item.raw.get("media", []):
        try:
            item.media.create(
                type=facebook_media_types[media["type"]], url=media["url"], raw=media
            )
        except DataError:
            print(media["url"])
