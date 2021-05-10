"""Api filters file."""
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from django_filters import Filter, FilterSet, filters

from apps.api.models import Dataset


class GroupByFilter(Filter):
    """Custom group by filter.

    Custom filter that provides the django groupby functionality
    on the given queryset.

    Parameters
    ----------
    Filter : django_filters
    """

    def filter(self, qs, value):
        """Group by filter method.

        Parameters
        ----------
        qs : django.db.models.query.QuerySet
            queryset on which group by filter is applied
        value : str
            comma separated group by filter values e.g 'channel,country'

        Returns
        -------
        django.db.models.query.QuerySet
            returns queryset based on the filtered values if value is given
            else returns original queryset
        """
        if value is None:
            return qs
        values = value.split(",")
        return qs.values(*values)


class AnnotateFilter(Filter):
    """Custom annotate filter.

    Custom filter that provides the django annotate functionality
    on the given queryset.
    It only provides the support of SUM function.

    Parameters
    ----------
    Filter : django_filters
    """

    def filter(self, qs, value):
        """Annotate filter method.

        Parameters
        ----------
        qs : django.db.models.query.QuerySet
            queryset on which annotate filter is applied
        value : str
            comma separated annotate filter values e.g 'impressions,clicks'

        Returns
        -------
        django.db.models.query.QuerySet
            returns queryset based on the filtered values if value is given
            else returns original queryset
        """
        if value is None:
            return qs
        filter = {val: Sum(val) for val in value.split(",")}
        return qs.annotate(**filter)


class CpiFilter(Filter):
    """Custom cpi filter.

    Custom filter that calculate the CPI value on the given queryset.

    Parameters
    ----------
    Filter : django_filters
    """

    def filter(self, qs, value):
        """CPI filter method.

        Parameters
        ----------
        qs : django.db.models.query.QuerySet
            queryset on which cpi is calculated
        value : bool
            it will be either true or false
        Returns
        -------
        django.db.models.query.QuerySet
            returns queryset based on the boolean value if true
            else returns original queryset
        """
        if value is None:
            return qs
        return qs.annotate(
            cpi=Cast(Sum("spend") / Sum("installs"), FloatField())
        )


class DataSetFilter(FilterSet):
    """Dataset filter class.

    A filtering class that provides multiple filters on the given data.

    Parameters
    ----------
    FilterSet : django_filters
    """

    date_to = filters.DateFilter(field_name="date", lookup_expr="lte")
    date_from = filters.DateFilter(field_name="date", lookup_expr="gte")
    channel = filters.CharFilter(field_name="channel", lookup_expr="exact")
    country = filters.CharFilter(field_name="country", lookup_expr="exact")
    os = filters.CharFilter(field_name="os", lookup_expr="exact")

    groupby = GroupByFilter()
    cpi = CpiFilter()
    annotate = AnnotateFilter()

    class Meta:  # noqa: D106
        model = Dataset
        fields = ["date_from", "date_to", "channel", "country", "os"]
