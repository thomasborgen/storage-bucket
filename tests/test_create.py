import uuid

import pytest
from google.api_core.exceptions import Conflict
from google.cloud.storage import Bucket
from returns.pipeline import is_successful

from storage_bucket.create import CreateBucket, create_bucket


def test_create_bucket_success():
    """Create bucket, get Success Modal."""
    bucket_result = CreateBucket()(
        storage_bucket_name='create-test-{id}'.format(id=uuid.uuid1()),
        location='EU',
    )
    assert is_successful(bucket_result)
    assert isinstance(bucket_result.unwrap(), Bucket)


def test_create_bucket():
    """Create container, get bucket."""
    bucket_result = create_bucket(
        storage_bucket_name='create-test-{id}'.format(id=uuid.uuid1()),
        location='EU',
    )
    assert isinstance(bucket_result, Bucket)


def test_create_bucket_failure_conflict():
    """Conflicting name, get Failure modal with Conflict exception."""
    bucket_result = CreateBucket()(
        storage_bucket_name='python-storage-bucket-test',
        location='EU',
    )
    assert not is_successful(bucket_result)
    assert isinstance(bucket_result.failure(), Conflict)


def test_create_bucket_exception_conflict():
    """Test that we get exception raised when we try to create existing."""
    with pytest.raises(Conflict):
        create_bucket(
            storage_bucket_name='python-storage-bucket-test',
            location='EU',
        )
