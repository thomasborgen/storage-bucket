# -*- coding: utf-8 -*-

"""Test Storage bucket classes."""

import uuid

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.create import CreateBucket
from storage_bucket.list import ListBuckets, list_bucket_names
from storage_bucket.delete import DeleteBucket, delete_bucket


@pytest.fixture
def deletable_bucket() -> str:
    """Create a deletable file and return its name."""
    bucket_name = 'delete-test-{uuid}'.format(uuid=uuid.uuid1())
    return CreateBucket()(
        storage_bucket_name=bucket_name,
        location='EU',
    ).map(
        lambda _: bucket_name,
    ).unwrap()


def test_delete_bucket_success(deletable_bucket):
    """Delete bucket, get Success Modal."""
    delete_result = DeleteBucket()(
        storage_bucket_name=deletable_bucket,
    )
    assert is_successful(delete_result)
    assert delete_result.unwrap() is None


def test_delete_bucket_does_not_exist_failure():
    """Conflicting name, get Failure modal with Conflict exception."""
    bucket_result = DeleteBucket()(
        storage_bucket_name='does-not-exist-{uuid}'.format(uuid=uuid.uuid1()),
    )
    assert not is_successful(bucket_result)
    assert isinstance(bucket_result.failure(), NotFound)


def test_delete_bucket_non_modal(deletable_bucket):
    """Test that we get exception raised when we try to create existing."""
    assert delete_bucket(  # type: ignore
        storage_bucket_name=deletable_bucket,
    ) is None


def test_delete_bucket_non_modal_not_exist_raises():
    """Test that we get exception raised when we try to create existing."""
    with pytest.raises(NotFound):
        delete_bucket(
            storage_bucket_name='does-not-exist-{uuid}'.format(
                uuid=uuid.uuid1(),
            ),
        )


def test_delete_multiple_buckets():
    """Clean up from create bucket test."""
    buckets = ListBuckets()(prefix='create-test-').map(
        list_bucket_names,
    ).unwrap()

    for bucket in buckets:
        delete_result = DeleteBucket()(storage_bucket_name=bucket).alt(
            print,  # noqa: T001
        )
        assert is_successful(delete_result)
