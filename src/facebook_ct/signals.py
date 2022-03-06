from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender="core.MemoSource")
def on_source_save(sender, instance, created, **kwargs):
    if not created:
        return
    # add task here
