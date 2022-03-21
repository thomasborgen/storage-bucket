import pytest
from google.api_core.exceptions import NotFound

from storage_bucket.download_file import download_file


def test_download_file_function(bucket_with_files):
    """Test downloading a file returns bytes."""
    assert download_file(
        storage_bucket_name=bucket_with_files[0],
        filename=bucket_with_files[1][0],
    ) == b'a'


def test_download_file_function_raises(existing_bucket):
    """Test downloading non-existing file raises NotFound exception."""
    with pytest.raises(NotFound):
        download_file(
            storage_bucket_name=existing_bucket,
            filename='does not exist.txt',
        )
