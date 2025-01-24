import pytest
from google.api_core.exceptions import Conflict
from google.cloud.storage import Bucket
from typing_extensions import Final

from storage_bucket.create import create_bucket

LOCATION: Final[str] = "EU"


def test_create_bucket_function(creatable_bucket):
    """Create bucket returns Bucket."""
    bucket_result = create_bucket(
        storage_bucket_name=creatable_bucket,
        location=LOCATION,
    )
    assert isinstance(bucket_result, Bucket)


def test_create_bucket_function_exception(existing_bucket):
    """Conflicting name raises Conflict exception."""
    with pytest.raises(Conflict):
        create_bucket(
            storage_bucket_name=existing_bucket,
            location=LOCATION,
        )
