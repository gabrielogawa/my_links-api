from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Link
from .serializer import LinkSerializer
from django.shortcuts import get_object_or_404
import ipdb
from tags.models import Tag
from rest_framework.response import Response
from rest_framework import status


class LinkView(ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get(self, req) -> Response:
        links = Link.objects.all()
        tag_name = req.query_params.get("tag", None)
        if tag_name:
            link_list = list(links)
            link_result = []
            for link in link_list:
                tag_link = link.tags.all()
                for tag in tag_link:
                    if tag.tag_name == tag_name:
                        link_result.append(link)
            result_page = self.paginate_queryset(link_result)
            serializer = LinkSerializer(result_page, many=True)
            return self.get_paginated_response(serializer.data)

        result_page = self.paginate_queryset(links)
        serializer = LinkSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)


class LinkDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def update(self, req, *args, **kwargs) -> Link:
        link = get_object_or_404(Link, id=self.kwargs["pk"])
        serializer = LinkSerializer(data=req.data, partial=True)

        serializer.is_valid()

        if not serializer.validated_data:
            return Response(
                {"message": "Dados incorretos"}, status=status.HTTP_400_BAD_REQUEST
            )

        tags_data = serializer.validated_data.pop("tags", None)

        if tags_data:
            tags = []
            for tag in tags_data:
                tag_obj = Tag.objects.filter(tag_name__iexact=tag["tag_name"]).first()

                if not tag_obj:
                    tag_obj = Tag.objects.create(**tag)
                    tags.append(tag_obj)

                tags.append(tag_obj)
            link.tags.set(tags)
        for key, value in serializer.validated_data.items():
            setattr(link, key, value)

        link.save()

        serializer = LinkSerializer(link)

        return Response(serializer.data)
