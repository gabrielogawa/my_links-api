from django.db import models


class Tag(models.Model):
    class Meta:
        ordering = ("id",)

    tag_name = models.CharField(max_length=250)
