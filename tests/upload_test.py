# -*- coding: utf-8 -*-

"""Test Storage bucket classes."""
import os
from typing import Final

import pytest
from google.api_core.exceptions import BadRequest, NotFound
from returns.pipeline import is_successful

from storage_bucket.upload_file import UploadFile, upload_file

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'not_set')


class TestStorageBucket(object):
    """Test stuff."""

    def test_upload_txt_file(self):
        """Test upload ok."""
        file_data = b'test'
        upload_result = UploadFile()(
            file_data,
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='txt_files/test.txt',
            content_type='plain/text',
        )
        assert is_successful(upload_result)

    def test_upload_xml_file(self):
        """Test upload ok."""
        file_data = b'<xml>test</xml>'
        upload_result = UploadFile()(
            file_data,
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='xml_files/test.xml',
            content_type='application/xml',
        )
        assert is_successful(upload_result)

    def test_upload_failure_bucket_does_not_exist(self):
        """Test upload failure."""
        file_data = None
        with open('tests/files/test.txt', 'rb') as o_file:
            file_data = o_file.read()
        upload_result = UploadFile()(
            file_data,
            storage_bucket_name='bucket-does-not-exist-in-project',
            filename='txt_files/test.txt',
            content_type='plain/text',
        )
        assert not is_successful(upload_result)
        assert isinstance(upload_result.failure(), NotFound)

    def test_upload_failure_bad_data(self):
        """Test upload failure."""
        file_data = 123
        upload_result = UploadFile()(
            file_data,  # type: ignore
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='txt_files/test.txt',
            content_type='plain/text',
        )
        assert not is_successful(upload_result)
        assert isinstance(upload_result.failure(), TypeError)

    def test_upload_failure_no_filename(self):
        """Test upload failure."""
        file_data = b'test'
        upload_result = UploadFile()(
            file_data,
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename=None,  # type: ignore
            content_type='plain/text',
        )
        assert not is_successful(upload_result)
        assert isinstance(upload_result.failure(), ValueError)

    def test_upload_failure_empty_filename(self):
        """Test upload failure."""
        file_data = b'test'
        upload_result = UploadFile()(
            file_data,
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='',
            content_type='plain/text',
        )
        assert not is_successful(upload_result)
        assert isinstance(upload_result.failure(), BadRequest)

    def test_upload_no_container(self):
        """Test upload failure."""
        file_data = b'test'
        upload_result = upload_file(
            file_data,
            storage_bucket_name=STORAGE_BUCKET_NAME,
            filename='txt_files/test2.txt',
            content_type='plain/text',
        )
        assert upload_result

    def test_upload_no_container_raises(self):
        """Test upload failure."""
        file_data = b'test'
        with pytest.raises(BadRequest):
            upload_file(
                file_data,
                storage_bucket_name=STORAGE_BUCKET_NAME,
                filename='',
                content_type='plain/text',
            )
