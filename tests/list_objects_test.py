# -*- coding: utf-8 -*-

"""Test Storage bucket classes."""
import os
from typing import Final

import pytest
from google.api_core.exceptions import NotFound
from returns.pipeline import is_successful

from storage_bucket.list_files import ListFiles, list_files

STORAGE_BUCKET_NAME: Final[str] = os.getenv('STORAGE_BUCKET_NAME', 'bad_name')


class TestListingObjects(object):
    """Test stuff."""

    def test_list_files(self):
        """Test that we can list files in a storage bucket."""
        files = ListFiles()(
            storage_bucket_name=STORAGE_BUCKET_NAME,
        )
        assert is_successful(files)
        assert isinstance(files.unwrap(), set)

    def test_list_files_failure(self):
        """Test that we get failure when bad storage bucket."""
        files = ListFiles()(
            storage_bucket_name='bucket-does-not-exist-in-project',
        )
        assert not is_successful(files)
        assert isinstance(files.failure(), NotFound)

    def test_list_files_with_prefix(self):
        """Test that we only get files with a certain prefix."""
        files = ListFiles()(
            storage_bucket_name=STORAGE_BUCKET_NAME,
            prefix='txt_files',
        )
        assert is_successful(files)

    def test_list_files_without_container(self):
        """Test that we can list files in a storage bucket."""
        files = list_files(
            storage_bucket_name=STORAGE_BUCKET_NAME,
        )
        assert isinstance(files, set)

    def test_list_files_without_container_raises(self):
        """Test that exception is raised."""
        with pytest.raises(NotFound):
            list_files(
                storage_bucket_name='bucket-does-not-exist-in-project',
            )
