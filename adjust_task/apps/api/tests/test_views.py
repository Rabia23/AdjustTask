"""Views test cases."""
import ddt
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.api.models import Dataset


@ddt.ddt
class SearchListViewTestCase(TestCase):
    """Search list view test cases.

    Parameters
    ----------
    TestCase : django.test
    """

    def setUp(self):
        """Set up the api url and database records for each
        test case.
        """
        self.url = reverse("search")
        self.datasets = [
            {
                "date": "2017-05-17",
                "channel": "adcolony",
                "country": "US",
                "os": "android",
                "impressions": "20",
                "clicks": "10",
                "installs": "50",
                "spend": "148.2",
                "revenue": "149.04",
            },
            {
                "date": "2017-05-17",
                "channel": "adcolony",
                "country": "US",
                "os": "ios",
                "impressions": "8",
                "clicks": "2",
                "installs": "50",
                "spend": "148.2",
                "revenue": "149.04",
            },
            {
                "date": "2017-05-17",
                "channel": "adcolony",
                "country": "ES",
                "os": "android",
                "impressions": "30",
                "clicks": "5",
                "installs": "50",
                "spend": "148.2",
                "revenue": "149.04",
            },
            {
                "date": "2017-05-14",
                "channel": "adcolony",
                "country": "US",
                "os": "ios",
                "impressions": "10",
                "clicks": "20",
                "installs": "50",
                "spend": "148.2",
                "revenue": "149.04",
            },
            {
                "date": "2017-05-16",
                "channel": "unityads",
                "country": "US",
                "os": "ios",
                "impressions": "40",
                "clicks": "7",
                "installs": "50",
                "spend": "148.2",
                "revenue": "149.04",
            },
        ]
        # create a list of dataset objects
        datasets = [Dataset(**row) for row in self.datasets]
        # insert records into the database
        Dataset.objects.bulk_create(datasets)

    def test_http_codes(self):
        """Test allowed or disallowed methods on the given url."""
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res = self.client.post(self.url)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        res = self.client.put(self.url)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_results_returns_all_elements(self):
        """Test that url returns all records if no filter is provided."""
        res = self.client.get(self.url)
        self.assertEqual(res.json()["count"], len(self.datasets))

    @ddt.data(
        ({"country": "US"}, 4),
        ({"country": "US", "os": "android", "channel": "adcolony"}, 1),
        ({"groupby": "country", "annotate": "clicks"}, 2),
        (
            {
                "date_to": "2017-06-01",
                "annotate": "impressions,clicks",
                "groupby": "channel,country",
                "ordering": "-clicks",
            },
            3,
        ),
        (
            {
                "date_from": "2017-05-01",
                "date_to": "2017-05-31",
                "os": "ios",
                "groupby": "date",
                "annotate": "installs",
                "ordering": "date",
            },
            3,
        ),
        (
            {
                "date_from": "2017-05-17",
                "date_to": "2017-05-17",
                "country": "US",
                "groupby": "os",
                "annotate": "revenue",
                "ordering": "-revenue",
            },
            2,
        ),
        (
            {
                "country": "US",
                "groupby": "channel",
                "cpi": True,
                "annotate": "spend",
                "ordering": "-cpi",
            },
            2,
        ),
    )
    @ddt.unpack
    def test_results_with_filters_returns_filtered_elements(
        self, params, expected_count
    ):
        """Test that url returns filtered records based on the
        provided filters.

        Parameters
        ----------
        params : dict
            filters for the given request
        expected_count : int
            count of rows returns by the filtered query
        """
        res = self.client.get(self.url, params)
        # assert that rows returns by the filtered query is equal to
        # expected count
        self.assertEqual(len(res.json()["results"]), expected_count)

    @ddt.data(
        {"dummy": "not_a_field"},
        {"groupby": "country;os"},
        {"annotate": "channell"},
        {"ordering": "-amount"},
        {"date_from": "2017-05-17", "date_to": "2017--06-01"},
    )
    def test_results_with_invalid_params_values_returns_400_response(
        self, params
    ):
        """Test that url returns 400 response code if invalid data
        is provided in the filters.

        Parameters
        ----------
        params : dict
            filters for the given request
        """
        res = self.client.get(self.url, params)
        # assert that response code returns by url is 400
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
