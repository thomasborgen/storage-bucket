import uuid

import pytest
from google.api_core.exceptions import NotFound
from google.cloud.storage import Bucket

from storage_bucket.get import GetBucket, get_bucket


def test_get_bucket_modal(existing_bucket):
    """Get bucket returns Success(Bucket)."""
    assert isinstance(GetBucket()(storage_bucket_name=existing_bucket), Bucket)


def test_get_bucket_function(existing_bucket):
    """Get bucket returns Bucket."""
    assert isinstance(get_bucket(storage_bucket_name=existing_bucket), Bucket)


def test_get_bucket_modal_failure():
    """Getting non-existant bucket should return Failure(NotFound)."""
    with pytest.raises(NotFound):
        GetBucket()(storage_bucket_name=uuid.uuid1().hex)


def test_get_bucket_function_raises():
    """Getting non-existant bucket should raise NotFound exception."""
    with pytest.raises(NotFound):
        get_bucket(storage_bucket_name=uuid.uuid1().hex)
