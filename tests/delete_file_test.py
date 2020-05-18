# -*- coding: utf-8 -*-

"""Test Storage bucket classes."""
import os
import uuid
from typing import Final

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.delete_file import DeleteFile, delete_file
from storage_bucket.upload_file import UploadFile

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


@pytest.fixture
def deletable_filename() -> str:
    """Create a deletable file and return its name."""
    filename = 'delete-test-{uuid}'.format(uuid=uuid.uuid1())
    return UploadFile()(
        b'data',
        STORAGE_BUCKET_NAME,
        filename,
    ).map(
        lambda _: filename,
    ).unwrap()


def test_delete_file(deletable_filename):
    """Test deleting a file returns Success."""
    delete_result = DeleteFile()(
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename=deletable_filename,
    )
    assert is_successful(delete_result)


def test_delete_non_existing_file_fails():
    """Test deleting a file."""
    delete_result = DeleteFile()(
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='filename-does-not-exists.test',
    )
    assert not is_successful(delete_result)
    assert isinstance(delete_result.failure(), NotFound)


def test_delete_non_existing_bucket_fails():
    """Test deleting a file."""
    delete_result = DeleteFile()(
        storage_bucket_name='bucket-does-not-exist',
        filename='test.txt',
    )
    assert not is_successful(delete_result)
    assert isinstance(delete_result.failure(), NotFound)


def test_delete_file_helper(deletable_filename):
    """Test deleting a file returns Success."""
    delete_result = delete_file(  # type: ignore
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename=deletable_filename,
    )
    assert delete_result is None


def test_delete_file_helper_raises():
    """Test deleting a file returns Success."""
    with pytest.raises(NotFound):
        delete_file(
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='filename-does-not-exists.test',
        )
