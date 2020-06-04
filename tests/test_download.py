import os
from typing import Final

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.download_file import DownloadFile, download_file

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


def test_download_file():
    """Test downloading a file and getting its data."""
    download_result = DownloadFile()(
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='txt_files/test.txt',
    )
    assert is_successful(download_result)
    assert download_result.unwrap() == b'test'


def test_download_file_without_container():
    """Test downloading a file without Result wrapping."""
    download_result = download_file(
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='txt_files/test.txt',
    )
    assert download_result == b'test'


def test_download_file_failure():
    """Test downloading a nonexistant file returns Failure."""
    download_result = DownloadFile()(
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='does not exist.txt',
    )
    assert not is_successful(download_result)
    assert isinstance(download_result.failure(), NotFound)


def test_download_file_without_container_raises():
    """Should raise NotFound exception."""
    with pytest.raises(NotFound):
        download_file(
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='does not exist.txt',
        )
