"""Api serializers file."""
from rest_framework import serializers

from apps.api.models import Dataset


class DataSetSerializer(serializers.ModelSerializer):
    """Dataset serializer class.

    Parameters
    ----------
    serializers : rest_framework
    """

    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    os = serializers.CharField(required=False)
    impressions = serializers.IntegerField(required=False, min_value=0)
    clicks = serializers.IntegerField(required=False, min_value=0)
    installs = serializers.IntegerField(required=False, min_value=0)
    spend = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2
    )
    revenue = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2
    )
    cpi = serializers.DecimalField(
        required=False, max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:  # noqa: D106
        model = Dataset
        fields = (
            "date",
            "channel",
            "country",
            "os",
            "impressions",
            "clicks",
            "installs",
            "spend",
            "revenue",
            "cpi",
        )
