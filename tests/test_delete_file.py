import os
import uuid
from typing import Final

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.delete_file import DeleteFile, delete_file

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


def test_delete_file_success(bucket_and_deletable_file):
    """Test deleting a file returns Success."""
    assert is_successful(DeleteFile()(
        storage_bucket_name=bucket_and_deletable_file[0],
        filename=bucket_and_deletable_file[1],
    ))


def test_delete_file_function_returns_none(bucket_and_deletable_file):
    """Test deleting a file returns Success."""
    assert delete_file(  # type: ignore
        storage_bucket_name=bucket_and_deletable_file[0],
        filename=bucket_and_deletable_file[1],
    ) is None


@pytest.mark.parametrize(('bucket', 'filename'), [
    # non-existing file
    (None, str(uuid.uuid1())),
    # non-existing bucket
    (str(uuid.uuid1()), 'test.xml'),
])
def test_delete_file_failure(existing_bucket, bucket, filename):
    """Test deleting a file gives failure."""
    delete_result = DeleteFile()(
        storage_bucket_name=bucket or existing_bucket,
        filename=filename,
    )
    assert not is_successful(delete_result)
    assert isinstance(delete_result.failure(), NotFound)


def test_delete_file_helper_raises():
    """Test deleting a file returns Success."""
    with pytest.raises(NotFound):
        delete_file(
            storage_bucket_name=str(uuid.uuid1()),
            filename=str(uuid.uuid1()),
        )
