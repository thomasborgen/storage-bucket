import pytest
from google.api_core.exceptions import NotFound

from storage_bucket.download_file import DownloadFile, download_file


def test_download_file_modal(bucket_with_files):
    """Test downloading a file returns Success(bytes)."""
    assert DownloadFile()(
        storage_bucket_name=bucket_with_files[0],
        filename=bucket_with_files[1][0],
    ).unwrap() == b'a'


def test_download_file_function(bucket_with_files):
    """Test downloading a file returns bytes."""
    assert download_file(
        storage_bucket_name=bucket_with_files[0],
        filename=bucket_with_files[1][0],
    ) == b'a'


def test_download_file_modal_failure(existing_bucket):
    """Test downloading a non-existant file returns Failure(NotFound)."""
    download_result = DownloadFile()(
        storage_bucket_name=existing_bucket,
        filename='does not exist.txt',
    )
    assert isinstance(download_result.failure(), NotFound)


def test_download_file_function_raises(existing_bucket):
    """Test downloading non-existing file raises NotFound exception."""
    with pytest.raises(NotFound):
        download_file(
            storage_bucket_name=existing_bucket,
            filename='does not exist.txt',
        )
