"""Api admin file."""
from django.contrib import admin

from apps.api.models import Dataset


class DatasetAdmin(admin.ModelAdmin):
    """Dataset model admin.

    Parameters
    ----------
    admin : django.contrib
    """

    list_display = ("id", "date", "country", "channel", "os")


admin.site.register(Dataset, DatasetAdmin)
