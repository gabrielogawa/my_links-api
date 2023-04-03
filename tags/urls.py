from django.urls import path
from .views import TagView, TagDetailView


urlpatterns = [
    path("tags/", TagView.as_view()),
    path("tags/<int:pk>/", TagDetailView.as_view()),
]
