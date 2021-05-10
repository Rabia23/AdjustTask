"""Models test cases."""
from django.db.utils import DataError
from django.test import TransactionTestCase

from apps.api.models import Dataset


class DatasetTestCase(TransactionTestCase):
    """Dataset model test cases.

    Parameters
    ----------
    TransactionTestCase : django.test
    """

    def test_creates_row_with_valid_data(self):
        """Test that row with the valid data successfully
        added in the database.
        """
        dataset_obj = {
            "date": "2017-05-17",
            "channel": "adcolony",
            "country": "US",
            "os": "android",
            "impressions": "19000",
            "clicks": "505",
            "installs": "190",
            "spend": "148.2",
            "revenue": "149.04",
        }
        dataset = Dataset.objects.create(**dataset_obj)
        # assert that one record is added in the db
        self.assertEqual(Dataset.objects.count(), 1)
        # assert that country inserted in the db is same as
        # dataset_obj country
        self.assertEqual(dataset.country, "US")

    def test_no_row_created_with_invalid_data(self):
        """Test that row with the invalid data doesn't added
        in the database.
        """
        dataset_obj = {
            "date": "2017-05-17",
            "channel": "adcolony",
            "country": "US",
            "os": "android",
            "impressions": "19000",
            "clicks": "-505",
            "installs": "190",
            "spend": "148.2",
            "revenue": "149.04",
        }
        expected_error_message = (
            "Out of range value for column 'clicks' at row 1"
        )
        with self.assertRaisesRegexp(DataError, expected_error_message):
            Dataset.objects.create(**dataset_obj)
        # assert that no row is added in the db
        self.assertFalse(Dataset.objects.exists())
