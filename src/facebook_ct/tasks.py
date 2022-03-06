from celery import shared_task
from purl import URL
from core.models import MemoItem, MemoSource
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
