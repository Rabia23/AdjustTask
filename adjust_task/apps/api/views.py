"""Api views file."""
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from apps.api.filters import DataSetFilter
from apps.api.models import Dataset
from apps.api.serializers import DataSetSerializer
from apps.pagination import StandardResultsSetPagination


@swagger_auto_schema(
    request_body=DataSetSerializer, responses={"200": DataSetSerializer}
)
class SearchListView(ListAPIView):
    """Search list view class.

    A HTTP api endpoint which is capable of filtering, grouping and sorting.

    Parameters
    ----------
    ListAPIView : rest_framework.generics

    Raises
    ------
    ValidationError
        if invalid data is passed in the query params
    """

    queryset = Dataset.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = DataSetSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = DataSetFilter
    permission_classes = [permissions.AllowAny]

    ordering_fields = [
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
    ]
    ordering = ["id"]

    def initial(self, request, *args, **kwargs):  # noqa: D401
        """
        Runs anything that needs to occur prior to calling the method handler.

        Parameters
        ----------
        request : django.http.request
        """
        super(SearchListView, self).initial(request, *args, **kwargs)
        # validates the query params
        self.validate()

    def validate(self):  # noqa: D401
        """
        Validates the query params in the given request.

        Raises
        ------
        ValidationError
            if data in the query params is invalid
        """
        GROUP_BY_CHOICES = ("date", "country", "channel", "os")
        ORDER_BY_CHOICES = (
            "date",
            "country",
            "channel",
            "os",
            "impressions",
            "clicks",
            "installs",
            "spend",
            "revenue",
            "cpi",
        )
        ANNOTATE_CHOICES = (
            "impressions",
            "clicks",
            "installs",
            "spend",
            "revenue",
        )

        valid_params = (
            "date_to",
            "date_from",
            "channel",
            "country",
            "os",
            "groupby",
            "cpi",
            "annotate",
            "ordering",
            "page",
        )
        valid_filters = {
            "groupby": GROUP_BY_CHOICES,
            "annotate": ANNOTATE_CHOICES,
            "ordering": ORDER_BY_CHOICES,
        }

        # get query parameters from the request object
        query_params = self.request.query_params

        if any(map(lambda x: x not in valid_params, query_params.keys())):
            raise ValidationError(
                {"error": f"Not a valid param. Options are {valid_params}"}
            )

        for filter, filter_choices in valid_filters.items():
            if filter in query_params:
                fields = query_params[filter].split(",")
                for field in fields:
                    # in case of ordering filter where - is used to
                    # sort in descending order
                    if field[0] == "-":
                        field = field[1:]
                    if field not in filter_choices:
                        raise ValidationError(
                            {
                                "error": f"{field} is not a valid {filter} "
                                "field value. If you are giving two values, "
                                "separate them with ','. Valid values are "
                                f"{filter_choices}."
                            }
                        )
