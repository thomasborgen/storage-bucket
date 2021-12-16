import uuid

import pytest

from storage_bucket.create import create_bucket
from storage_bucket.delete import delete_bucket
from storage_bucket.upload_file import upload_file


@pytest.fixture(scope='session')
def existing_bucket():
    """Create a bucket for use in tests. Delete when done.

    yields str
    """
    bucket_name = 'test-bucket-{uuid}'.format(uuid=uuid.uuid1())

    create_bucket(
        storage_bucket_name=bucket_name,
        location='EU',
    )
    yield bucket_name
    delete_bucket(storage_bucket_name=bucket_name, force=True)


@pytest.fixture(scope='function')
def creatable_bucket():
    """Create a random bucket name for use in tests.

    Deletes the bucket when done.
    yields str
    """
    bucket_name = 'test-bucket-{uuid}'.format(uuid=uuid.uuid1())
    yield bucket_name
    delete_bucket(storage_bucket_name=bucket_name, force=True)


@pytest.fixture(scope='function')
def deletable_bucket() -> str:
    """Create a deletable bucket and return its name.

    The bucket will be created so that a function can delete it
    yields str
    """
    bucket_name = 'delete-test-{uuid}'.format(uuid=uuid.uuid1())
    create_bucket(
        storage_bucket_name=bucket_name,
        location='EU',
    )
    return bucket_name


@pytest.fixture(scope='function')
def bucket_and_deletable_file(existing_bucket):
    """Create a deletable file and return its name.

    This file will be created in the bucket given by existing_bucket fixture
    The file will only live during the duration of the test function
    yields Tuple[str, str]
    """
    filename = 'delete-test-{uuid}'.format(uuid=uuid.uuid1())
    upload_file(
        file_content=b'data',
        storage_bucket_name=existing_bucket,
        filename=filename,
    )
    yield (existing_bucket, filename)


@pytest.fixture(scope='session')
def bucket_with_files(existing_bucket):
    """Create files in our test bucket for listing.

    The files should be used for listing or getting tests
    The files will live until testing is done.
    yields Tuple[str, Tuple[str...]]
    """
    filenames = (
        'test.txt',
        'path/{uuid}'.format(uuid=uuid.uuid1()),
    )

    for filename_create in filenames:
        upload_file(
            file_content=b'a',
            storage_bucket_name=existing_bucket,
            filename=filename_create,
        )
    yield (existing_bucket, filenames)
