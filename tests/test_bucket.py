import uuid

import pytest
from google.api_core.exceptions import NotFound
from google.cloud.storage import Bucket

from storage_bucket.bucket import get_bucket


def test_get_bucket(existing_bucket):
    """Get bucket returns Bucket."""
    assert isinstance(get_bucket(storage_bucket_name=existing_bucket), Bucket)


def test_get_bucket_function_raises():
    """Getting non-existant bucket should raise NotFound exception."""
    with pytest.raises(NotFound):
        get_bucket(storage_bucket_name=uuid.uuid1().hex)
