import uuid

import pytest
from google.api_core.exceptions import BadRequest, NotFound
from returns.pipeline import is_successful

from storage_bucket.upload_file import UploadFile, upload_file


@pytest.mark.parametrize(('data_bytes', 'filename', 'content_type'), [
    (b'a', 'test.txt', 'plain/text'),
    (b'<xml>a</xml>', 'test.xml', 'application/xml'),
    (b'a', 'test.txt', None),
])
def test_upload(existing_bucket, data_bytes, filename, content_type):
    """Test upload ok."""
    assert is_successful(
        UploadFile()(
            data_bytes,
            storage_bucket_name=existing_bucket,
            filename=filename,
            content_type=content_type,
        ),
    )


def test_upload_unsafe(existing_bucket):
    """Uploading unsafely returns None on success."""
    assert upload_file(  # type: ignore
        b'd',
        storage_bucket_name=existing_bucket,
        filename='filename.txt',
    ) is None


@pytest.mark.parametrize(('raw_data', 'filename', 'bucket', 'expected'), [
    # bucket does not exist
    (b'test', 'test.txt', str(uuid.uuid1()), NotFound),
    # bad data type
    (123, 'test.xml', None, TypeError),
    # bad filename
    (b'test', None, None, ValueError),
    # bad request on empty filename
    (b'test', '', None, BadRequest),
])
def test_upload_failure(existing_bucket, raw_data, filename, bucket, expected):
    """Test upload failure."""
    assert isinstance(
        UploadFile()(
            raw_data,
            storage_bucket_name=bucket or existing_bucket,
            filename=filename,
        ).failure(),
        expected,
    )


def test_upload_unsafely_raises():
    """Test upload failure raises exception."""
    with pytest.raises(NotFound):
        upload_file(
            b'test',
            storage_bucket_name=str(uuid.uuid1()),
            filename='test.txt',
            content_type='plain/text',
        )
