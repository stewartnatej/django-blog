from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path(
        "", PollListView.as_view(), name="poll_index"
    ),  # empty string is root (relative to polling)
    path("polls/<int:pk>", PollDetailView.as_view(), name="poll_detail"),
]
