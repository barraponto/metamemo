from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


class MetaMemo(models.Model):
    """Represent the actual metamemo profile."""

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class MemoSource(models.Model):
    """A (social) media source for a given profile."""

    name = models.CharField(max_length=256)
    url = models.URLField(max_length=256)
    memo = models.ForeignKey(MetaMemo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.memo.name}: {self.name}"


class MemoItem(models.Model):
    """A memo item from a given source, with optional media."""

    url = models.URLField(max_length=512)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)
    extracted = models.DateTimeField(auto_now_add=True)
    raw = models.JSONField(encoder=DjangoJSONEncoder, null=True)
    source = models.ForeignKey(MemoSource, on_delete=models.CASCADE)


class MemoMedia(models.Model):
    """Extracted media files from memo items."""

    class MediaTypes(models.TextChoices):
        VIDEO = "VIDEO", "Video"
        IMAGE = "IMAGE", "Image"

    type = models.CharField(max_length=8, choices=MediaTypes.choices)
    url = models.URLField(max_length=512)
    media = models.FileField(upload_to="media")
