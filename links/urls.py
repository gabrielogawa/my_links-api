from django.urls import path
from .views import LinkView, LinkDetailView


urlpatterns = [
    path("links/", LinkView.as_view()),
    path("links/<int:pk>/", LinkDetailView.as_view()),
]
