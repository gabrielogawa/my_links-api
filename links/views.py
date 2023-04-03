from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Link
from .serializer import LinkSerializer


class LinkView(ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkDetailView(RetrieveUpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
