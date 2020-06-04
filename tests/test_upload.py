import os
from typing import Final

import pytest
from google.api_core.exceptions import BadRequest, NotFound
from returns.pipeline import is_successful

from storage_bucket.upload_file import UploadFile, upload_file

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


@pytest.mark.parametrize(('data_bytes', 'filename', 'content_type'), [
    (b'test', 'test.txt', 'plain/text'),
    (b'<xml>test</xml>', 'test.xml', 'application/xml'),
])
def test_upload_xml_file(data_bytes, filename, content_type):
    """Test upload ok."""
    upload_result = UploadFile()(
        data_bytes,
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename=filename,
        content_type=content_type,
    )
    assert is_successful(upload_result)


def test_upload_txt_file_no_container():
    """Test upload ok with normal function."""
    assert upload_file(  # type: ignore
        b'<xml>test</xml>',
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='xml_files/test.xml',
        content_type='application/xml',
    ) is None


@pytest.mark.parametrize(('raw_data', 'filename', 'bucket', 'expected'), [
    # bucket does not exist
    (b'test', 'test.txt', 'bucket-does-not-exist-123', NotFound),
    # bad data type
    (123, 'test.xml', STORAGE_BUCKET_NAME, TypeError),
    # bad filename
    (b'test', None, STORAGE_BUCKET_NAME, ValueError),
    # bad request on empty filename
    (b'test', '', STORAGE_BUCKET_NAME, BadRequest),
])
def test_upload_failure(raw_data, filename, bucket, expected):
    """Test upload failure."""
    upload_result = UploadFile()(
        raw_data,
        storage_bucket_name=bucket,
        filename=filename,
        content_type='plain/text',
    )
    assert not is_successful(upload_result)
    assert isinstance(upload_result.failure(), expected)


def test_upload_no_container():
    """Test upload succeedes."""
    upload_result = upload_file(  # type: ignore
        b'test',
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='txt_files/test2.txt',
        content_type='plain/text',
    )
    assert upload_result is None


def test_upload_no_container_raises():
    """Test upload failure raises exception."""
    with pytest.raises(BadRequest):
        upload_file(
            b'test',
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='',
            content_type='plain/text',
        )
