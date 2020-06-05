import uuid

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.list_files import ListFiles, list_files


def test_list_files(bucket_with_listable_files):
    """Test that we can list files in a storage bucket."""
    files = ListFiles()(
        storage_bucket_name=bucket_with_listable_files,
    )
    assert is_successful(files)
    assert isinstance(files.unwrap(), set)


def test_list_files_with_prefix(bucket_with_listable_files):
    """Test that we only get files with a certain prefix."""
    files = ListFiles()(
        storage_bucket_name=bucket_with_listable_files,
        prefix='path1',
    )
    assert is_successful(files)


def test_list_files_without_container(bucket_with_listable_files):
    """Test that we can list files in a storage bucket."""
    files = list_files(
        storage_bucket_name=bucket_with_listable_files,
    )
    assert isinstance(files, set)


def test_list_files_failure():
    """Test that we get failure when bad storage bucket."""
    files = ListFiles()(
        storage_bucket_name=str(uuid.uuid1()),
    )
    assert not is_successful(files)
    assert isinstance(files.failure(), NotFound)


def test_list_files_without_container_raises():
    """Test that exception is raised."""
    with pytest.raises(NotFound):
        list_files(
            storage_bucket_name=str(uuid.uuid1()),
        )
