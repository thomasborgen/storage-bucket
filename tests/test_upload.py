import uuid

import pytest
from google.api_core.exceptions import BadRequest, NotFound

from storage_bucket.upload_file import upload_file


def test_upload_file(existing_bucket):
    """Uploading returns None on success."""
    assert (
        upload_file(  # type: ignore
            file_content=b"d",
            storage_bucket_name=existing_bucket,
            filename="filename.txt",
        )
        is None
    )


@pytest.mark.parametrize(
    ("raw_data", "filename", "bucket", "expected"),
    [
        # bucket does not exist
        (b"test", "test.txt", uuid.uuid1().hex, NotFound),
        # bad data type
        (123, "test.xml", None, TypeError),
        # bad filename
        (b"test", None, None, ValueError),
        # bad request on empty filename
        (b"test", "", None, BadRequest),
    ],
)
def test_upload_file_failure(
    existing_bucket,
    raw_data,
    filename,
    bucket,
    expected,
):
    """Test upload failure."""
    with pytest.raises(expected):
        upload_file(
            file_content=raw_data,
            storage_bucket_name=bucket or existing_bucket,
            filename=filename,
        )
