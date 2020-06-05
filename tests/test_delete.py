import uuid

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.delete import DeleteBucket, delete_bucket


def test_delete_bucket_success(deletable_bucket):
    """Delete bucket, get Success Modal."""
    assert is_successful(DeleteBucket()(storage_bucket_name=deletable_bucket))


def test_delete_bucket_unsafe(deletable_bucket):
    """Delete bucket unsafely."""
    assert delete_bucket(  # type: ignore
        storage_bucket_name=deletable_bucket,
    ) is None


def test_delete_bucket_failure():
    """Does not exist."""
    assert isinstance(
        DeleteBucket()(storage_bucket_name=str(uuid.uuid1())).failure(),
        NotFound,
    )


def test_delete_bucket_unsafe_raises():
    """Does not exist."""
    with pytest.raises(NotFound):
        delete_bucket(storage_bucket_name=str(uuid.uuid1()))
