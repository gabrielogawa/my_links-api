from rest_framework import serializers
from .models import Link
from tags.serializer import TagSerializer
from tags.models import Tag


class LinkSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        tags = []
        for tag in tags_data:
            tag_dict = dict(tag)
            tag_obj = Tag.objects.filter(tag_name__iexact=tag_dict["tag_name"]).first()
            if not tag_obj:
                tag_obj = Tag.objects.create(**tag_dict)
                tags.append(tag_obj)
            tags.append(tag_obj)
        link = Link.objects.create(**validated_data)
        link.tags.set(tags)

        return link

    tags = TagSerializer(many=True)

    class Meta:
        model = Link
        fields = ["id", "url", "tags"]
