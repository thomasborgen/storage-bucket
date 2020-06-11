import uuid

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.list_files import ListFiles, list_files


def test_list_files_modal(bucket_with_files):
    """Test that we can list files in a storage bucket."""
    files = ListFiles()(bucket_with_files)
    assert isinstance(files.unwrap(), set)


def test_list_files_modal_with_prefix(bucket_with_files):
    """Test that we only get files with a certain prefix."""
    files = ListFiles()(bucket_with_files, prefix='path1')
    assert is_successful(files)
    assert all('path1' in blob.name for blob in files.unwrap())


def test_list_files_function(bucket_with_files):
    """Test that we can list files in a storage bucket."""
    assert isinstance(list_files(bucket_with_files), set)


def test_list_files_modal_failure():
    """Test that we get failure when bad storage bucket."""
    files = ListFiles()(uuid.uuid1().hex)
    assert isinstance(files.failure(), NotFound)


def test_list_files_function_raises():
    """Test that NotFound exception is raised."""
    with pytest.raises(NotFound):
        list_files(uuid.uuid1().hex)
