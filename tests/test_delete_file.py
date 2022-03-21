import uuid

import pytest
from google.api_core.exceptions import NotFound

from storage_bucket.delete_file import delete_file


def test_delete_file_function(bucket_and_deletable_file):
    """Test deleting a file okay returns None."""
    assert delete_file(  # type: ignore
        storage_bucket_name=bucket_and_deletable_file[0],
        filename=bucket_and_deletable_file[1],
    ) is None


def test_delete_file_raises_when_no_such_file(existing_bucket):
    """Test deleting a non-existing file raises NotFound Exception."""
    with pytest.raises(NotFound):
        delete_file(
            storage_bucket_name=existing_bucket,
            filename=uuid.uuid1().hex,
        )


def test_delete_file_raises_when_no_such_bucket():
    """Test deleting a file in bad bucket returns Failure(NotFound)."""
    with pytest.raises(NotFound):
        delete_file(
            storage_bucket_name=uuid.uuid1().hex,
            filename='test.txt',
        )
