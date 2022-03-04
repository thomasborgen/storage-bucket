import uuid

import pytest
from google.api_core.exceptions import NotFound

from storage_bucket.list_files import list_files


def test_list_files_function(bucket_with_files):
    """Test that we can list files in a storage bucket."""
    assert isinstance(list_files(storage_bucket_name=bucket_with_files[0]), set)


def test_list_files_with_prefix(bucket_with_files):
    """Test that we only get files with a certain prefix."""
    files = list_files(
        storage_bucket_name=bucket_with_files[0],
        prefix='path',
    )
    assert {blob.name for blob in files}.issubset(
        bucket_with_files[1],
    )


def test_list_files_function_raises():
    """Test that NotFound exception is raised."""
    with pytest.raises(NotFound):
        list_files(storage_bucket_name=uuid.uuid1().hex)
