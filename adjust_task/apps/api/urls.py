"""Api urls file."""
from django.urls import path

from apps.api.views import SearchListView

urlpatterns = [
    path("search/", SearchListView.as_view(), name="search"),
]
