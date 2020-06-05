import pytest
from google.api_core.exceptions import Conflict
from google.cloud.storage import Bucket

from storage_bucket.create import CreateBucket, create_bucket


def test_create_bucket_success(creatable_bucket):
    """Create bucket, get Success Modal."""
    bucket_result = CreateBucket()(
        storage_bucket_name=creatable_bucket,
        location='EU',
    )
    assert isinstance(bucket_result.unwrap(), Bucket)


def test_create_bucket(creatable_bucket):
    """Create container, get bucket."""
    bucket_result = create_bucket(
        storage_bucket_name=creatable_bucket,
        location='EU',
    )
    assert isinstance(bucket_result, Bucket)


def test_create_bucket_failure_conflict(existing_bucket):
    """Conflicting name, get Failure modal with Conflict exception."""
    bucket_result = CreateBucket()(
        storage_bucket_name=existing_bucket,
        location='EU',
    )
    assert isinstance(bucket_result.failure(), Conflict)


def test_create_bucket_exception_conflict(existing_bucket):
    """Test that we get exception raised when we try to create existing."""
    with pytest.raises(Conflict):
        create_bucket(
            storage_bucket_name=existing_bucket,
            location='EU',
        )
