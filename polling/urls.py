from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="poll_index"),  # empty string is root (relative to polling)
    path('polls/<int:poll_id>', detail_view, name='poll_detail')
]
