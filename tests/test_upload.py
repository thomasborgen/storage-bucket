import os
from typing import Final

import pytest
from google.api_core.exceptions import BadRequest, NotFound
from returns.pipeline import is_successful

from storage_bucket.upload_file import UploadFile, upload_file

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


def test_upload_txt_file():
    """Test upload ok."""
    upload_result = UploadFile()(
        b'test',
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='txt_files/test.txt',
        content_type='plain/text',
    )
    assert is_successful(upload_result)


def test_upload_xml_file():
    """Test upload ok."""
    upload_result = UploadFile()(
        b'<xml>test</xml>',
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='xml_files/test.xml',
        content_type='application/xml',
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


def test_upload_failure_bucket_does_not_exist():
    """Test upload failure."""
    upload_result = UploadFile()(
        b'test',
        storage_bucket_name='bucket-does-not-exist-in-project',
        filename='txt_files/test.txt',
        content_type='plain/text',
    )
    assert not is_successful(upload_result)
    assert isinstance(upload_result.failure(), NotFound)


def test_upload_failure_bad_data():
    """Test upload failure."""
    upload_result = UploadFile()(
        123,  # type: ignore # this is on purpose
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='txt_files/test.txt',
        content_type='plain/text',
    )
    assert not is_successful(upload_result)
    assert isinstance(upload_result.failure(), TypeError)


def test_upload_failure_no_filename():
    """Test upload failure."""
    upload_result = UploadFile()(
        b'test',
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename=None,  # type: ignore
        content_type='plain/text',
    )
    assert not is_successful(upload_result)
    assert isinstance(upload_result.failure(), ValueError)


def test_upload_failure_empty_filename():
    """Test upload failure."""
    upload_result = UploadFile()(
        b'test',
        storage_bucket_name=STORAGE_BUCKET_NAME,
        filename='',
        content_type='plain/text',
    )
    assert not is_successful(upload_result)
    assert isinstance(upload_result.failure(), BadRequest)


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
