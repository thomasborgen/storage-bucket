import uuid

import pytest
from google.api_core.exceptions import BadRequest, NotFound
from returns.pipeline import is_successful

from storage_bucket.upload_file import UploadFile, upload_file


def test_upload_file_modal(existing_bucket):
    """Test upload returns Success."""
    assert is_successful(
        UploadFile()(
            b'a',
            storage_bucket_name=existing_bucket,
            filename='test.txt',
        ),
    )


def test_upload_file_function(existing_bucket):
    """Uploading returns None on success."""
    assert upload_file(  # type: ignore
        b'd',
        storage_bucket_name=existing_bucket,
        filename='filename.txt',
    ) is None


@pytest.mark.parametrize(('raw_data', 'filename', 'bucket', 'expected'), [
    # bucket does not exist
    (b'test', 'test.txt', uuid.uuid1().hex, NotFound),
    # bad data type
    (123, 'test.xml', None, TypeError),
    # bad filename
    (b'test', None, None, ValueError),
    # bad request on empty filename
    (b'test', '', None, BadRequest),
])
def test_upload_file_modal_failure(
    existing_bucket, raw_data, filename, bucket, expected,
):
    """Test upload failure."""
    assert isinstance(
        UploadFile()(
            raw_data,
            storage_bucket_name=bucket or existing_bucket,
            filename=filename,
        ).failure(),
        expected,
    )


def test_upload_file_function_raises():
    """Test upload failure raises NotFound exception."""
    with pytest.raises(NotFound):
        upload_file(
            b'test',
            storage_bucket_name=str(uuid.uuid1()),
            filename='test.txt',
            content_type='plain/text',
        )
