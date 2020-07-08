import os

import pytest
from google.auth.exceptions import DefaultCredentialsError
from google.cloud.storage import Client
from typing_extensions import Final

from storage_bucket.client import get_client

ENV_VAR: Final[str] = 'GOOGLE_APPLICATION_CREDENTIALS'


def test_get_client_function():
    """Create bucket returns Bucket."""
    client_result = get_client()

    assert isinstance(client_result, Client)


def test_get_client_function_exception():
    """Conflicting name raises Conflict exception."""
    old = os.environ[ENV_VAR]
    os.environ[ENV_VAR] = 'badfile'
    with pytest.raises(DefaultCredentialsError):
        get_client()
    os.environ[ENV_VAR] = old
