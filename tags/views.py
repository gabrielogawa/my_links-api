from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Tag
from .serializer import TagSerializer


class TagView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(RetrieveUpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
