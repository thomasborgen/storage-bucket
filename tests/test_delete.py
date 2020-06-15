import uuid

import pytest
from google.api_core.exceptions import NotFound

from storage_bucket.delete import delete_bucket


def test_delete_bucket_function(deletable_bucket):
    """Delete bucket returns None."""
    assert delete_bucket(  # type: ignore
        storage_bucket_name=deletable_bucket,
    ) is None


def test_delete_bucket_function_raises():
    """Does not exist raises NotFound exception."""
    with pytest.raises(NotFound):
        delete_bucket(storage_bucket_name=uuid.uuid1().hex)
