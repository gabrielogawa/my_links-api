from django.db import models


class Link(models.Model):
    class Meta:
        ordering = ("id",)

    url = models.CharField(max_length=1000)
    tags = models.ManyToManyField("tags.Tag", related_name="links")
