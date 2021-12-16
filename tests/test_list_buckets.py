import pytest
from google.api_core.page_iterator import HTTPIterator
from google.cloud.storage.bucket import Bucket
from google.cloud.storage.client import Client

from storage_bucket.list import ListBuckets, list_bucket_names, list_buckets


def test_list_buckets_modal_found(existing_bucket):
    """Test that bucket is listed."""
    buckets = ListBuckets()()
    bucket_names = list_bucket_names(buckets)
    assert existing_bucket in bucket_names
    assert isinstance(buckets, HTTPIterator)


def test_list_buckets_modal_not_found():
    """Test that bucket is not listed."""
    buckets = ListBuckets()()
    bucket_names = list_bucket_names(buckets)
    assert 'not_in_use' not in bucket_names


def test_list_buckets_function_found(existing_bucket):
    """Test that bucket is listed."""
    buckets = list_buckets()
    bucket_names = list_bucket_names(buckets)
    assert existing_bucket in bucket_names
    assert isinstance(buckets, HTTPIterator)


def test_list_buckets_function_not_found(existing_bucket):
    """Test that bucket is not listed."""
    buckets = list_buckets()
    bucket_names = list_bucket_names(buckets)
    assert 'not_in_use' not in bucket_names


def test_list_bucket_names(existing_bucket):
    """Test that mapping returns correct names."""
    buckets = {Bucket(client=Client(), name=existing_bucket)}
    assert existing_bucket in list_bucket_names(buckets)


def test_list_bucket_names_no_buckets():
    """Test when buckets are None."""
    with pytest.raises(AttributeError):
        set(el for el in list_bucket_names({None}))  # noqa: WPS428, C401
