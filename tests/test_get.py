# -*- coding: utf-8 -*-

"""Test Get Storage bucket class."""
import uuid

import pytest
from google.api_core.exceptions import NotFound
from google.cloud.storage import Bucket
from returns.pipeline import is_successful

from storage_bucket.get import GetBucket, get_bucket


def test_get_bucket_success(existing_bucket):
    """Create bucket, get Success Modal."""
    assert is_successful(
        GetBucket()(storage_bucket_name=existing_bucket),
    )


def test_get_bucket(existing_bucket):
    """Create container, get bucket."""
    bucket_result = get_bucket(
        storage_bucket_name=existing_bucket,
    )
    assert isinstance(bucket_result, Bucket)


def test_get_bucket_failure():
    """Getting non-existant bucket should give NotFound failure."""
    assert isinstance(
        GetBucket()(storage_bucket_name=str(uuid.uuid1())).failure(),
        NotFound,
    )


def test_get_bucket_raises():
    """Getting non-existant bucket should raise NotFound."""
    with pytest.raises(NotFound):
        get_bucket(storage_bucket_name=str(uuid.uuid1()))
