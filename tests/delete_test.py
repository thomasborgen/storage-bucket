# -*- coding: utf-8 -*-

"""Test Storage bucket classes."""

import pytest
from google.api_core.exceptions import Conflict
from google.cloud.storage import Bucket
from returns.pipeline import is_successful

from storage_bucket.delete import DeleteBucket, delete_bucket


class TestDeletingBuckets(object):
    """Test stuff."""

    def stest_create_bucket_success(self):
        """Create bucket, get Success Modal."""
        bucket_result = DeleteBucket()(
            storage_bucket_name='',
        )
        assert is_successful(bucket_result)
        assert isinstance(bucket_result.unwrap(), Bucket)

    def stest_create_bucket_failure_conflict(self):
        """Conflicting name, get Failure modal with Conflict exception."""
        bucket_result = DeleteBucket()(
            storage_bucket_name='python-storage-bucket-test',
        )
        assert not is_successful(bucket_result)
        assert isinstance(bucket_result.failure(), Conflict)

    def tsest_create_bucket_exception_conflict(self):
        """Test that we get exception raised when we try to create existing."""
        with pytest.raises(Conflict):
            delete_bucket(
                storage_bucket_name='python-storage-bucket-test',
            )
