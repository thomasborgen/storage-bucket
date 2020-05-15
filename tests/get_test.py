# -*- coding: utf-8 -*-

"""Test Get Storage bucket class."""
import pytest
from google.api_core.exceptions import NotFound
from google.cloud.storage import Bucket
from returns.pipeline import is_successful

from storage_bucket.get import GetBucket, get_bucket


class TestGetBucket(object):
    """Test Get Bucket."""

    def test_get_bucket_success(self):
        """Create bucket, get Success Modal."""
        bucket_result = GetBucket()(
            storage_bucket_name='test-bucket-my-name-is',
        )
        assert is_successful(bucket_result)
        assert isinstance(bucket_result.unwrap(), Bucket)

    def test_create_get_failure_conflict(self):
        """Conflicting name, get Failure modal with Conflict exception."""
        bucket_result = GetBucket()(
            storage_bucket_name='test-bucket-with-my-name',
        )
        assert not is_successful(bucket_result)
        assert isinstance(bucket_result.failure(), NotFound)

    def test_get_bucket(self):
        """Create container, get bucket."""
        bucket_result = get_bucket(
            storage_bucket_name='test-bucket-my-name-is',
        )
        assert isinstance(bucket_result, Bucket)

    def test_get_bucket_exception_conflict(self):
        """Test that we get exception raised when we try to create existing."""
        with pytest.raises(NotFound):
            get_bucket(
                storage_bucket_name='test-bucket-with-my-name',
            )
