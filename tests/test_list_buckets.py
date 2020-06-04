import os
from typing import Final

import pytest
from google.api_core.page_iterator import HTTPIterator
from google.cloud.storage.bucket import Bucket
from google.cloud.storage.client import Client

from storage_bucket.list import ListBuckets, list_bucket_names, list_buckets

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


def test_list_buckets_success_found():
    """Test that bucket is listed."""
    buckets = ListBuckets()()
    bucket_names = list_bucket_names(buckets.unwrap())
    assert STORAGE_BUCKET_NAME in bucket_names
    assert isinstance(buckets.unwrap(), HTTPIterator)


def test_list_buckets_success_not_found():
    """Test that bucket is not listed."""
    buckets = ListBuckets()()
    bucket_names = list_bucket_names(buckets.unwrap())
    assert 'not_in_use' not in bucket_names


def test_list_buckets_found():
    """Test that bucket is listed."""
    buckets = list_buckets()
    bucket_names = list_bucket_names(buckets)
    assert STORAGE_BUCKET_NAME in bucket_names
    assert isinstance(buckets, HTTPIterator)


def test_list_buckets_not_found():
    """Test that bucket is not listed."""
    buckets = list_buckets()
    bucket_names = list_bucket_names(buckets)
    assert 'not_in_use' not in bucket_names


def test_list_bucket_names():
    """Test that mapping returns correct names."""
    buckets = {Bucket(client=Client(), name=STORAGE_BUCKET_NAME)}
    assert STORAGE_BUCKET_NAME in list_bucket_names(buckets)


def test_list_bucket_names_no_buckets():
    """Test when buckets are None."""
    with pytest.raises(AttributeError):
        set(el for el in list_bucket_names({None}))  # noqa: WPS428, C401
