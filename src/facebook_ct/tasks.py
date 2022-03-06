from celery import shared_task
from django.core.files import File
from purl import URL

from core.models import MemoItem, MemoMedia, MemoSource
from .api import FBCrowdTangleAPI
from core.utils import streaming_download


@shared_task
def get_facebook_data(source_id):
    source = MemoSource.objects.get(pk=source_id)
    username = URL(source.url).path_segment(-1)
    for post in FBCrowdTangleAPI(username):
        item = MemoItem(
            url=post["postUrl"], created=post["date"], raw=post, source=source
        )
        item.save()


instagram_media_types = {
    "video": MemoMedia.MediaTypes.VIDEO,
    "photo": MemoMedia.MediaTypes.IMAGE,
}


@shared_task
def get_facebook_media(item_id):
    item = MemoItem.objects.get(pk=item_id)
    for media in item.raw.get("media", []):
        item.media.create(
            type=instagram_media_types[media["type"]], url=media["url"], raw=media
        )


@shared_task
def download_fbcdn_media(media_id):
    media = MemoMedia.objects.get(pk=media_id)

    username = URL(media.item.source.url).path_segment(-1)
    filename = URL(media.url).path_segment(-1)
    filepath = f"fbcdn_{username}_{filename}"

    with streaming_download(media.url) as tempfile:
        media.media.save(filepath, File(tempfile))
