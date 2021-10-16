import uuid

import pytest
from google.api_core.exceptions import NotFound

from storage_bucket.delete_file import DeleteFile, delete_file


def test_delete_file_modal(bucket_and_deletable_file):
    """Test deleting a file returns Success."""
    assert DeleteFile()(
        storage_bucket_name=bucket_and_deletable_file[0],
        filename=bucket_and_deletable_file[1],
    ) is None


def test_delete_file_function(bucket_and_deletable_file):
    """Test deleting a file okay returns None."""
    assert delete_file(  # type: ignore
        storage_bucket_name=bucket_and_deletable_file[0],
        filename=bucket_and_deletable_file[1],
    ) is None


def test_delete_file_modal_failure_no_file(existing_bucket):
    """Test deleting a non-existing file returns Failure(NotFound)."""
    with pytest.raises(NotFound):
        DeleteFile()(
            storage_bucket_name=existing_bucket,
            filename=uuid.uuid1().hex,
        )


def test_delete_file_modal_failure_no_bucket():
    """Test deleting a file in bad bucket returns Failure(NotFound)."""
    with pytest.raises(NotFound):
        DeleteFile()(
            storage_bucket_name=uuid.uuid1().hex,
            filename='test.txt',
        )


def test_delete_file_function_raises():
    """Test deleting a non-existing file raises NotFound exception."""
    with pytest.raises(NotFound):
        delete_file(
            storage_bucket_name=uuid.uuid1().hex,
            filename=uuid.uuid1().hex,
        )
