import uuid

import pytest

from storage_bucket.create import create_bucket
from storage_bucket.delete import delete_bucket
from storage_bucket.upload_file import upload_file


@pytest.fixture(scope='session')
def existing_bucket():
    """Create a bucket for use in tests. Delete when done."""
    bucket_name = 'test-bucket-{uuid}'.format(uuid=uuid.uuid1())

    create_bucket(bucket_name, 'EU')
    yield bucket_name
    delete_bucket(bucket_name, force=True)


@pytest.fixture(scope='function')
def creatable_bucket():
    """Create a random bucket name for use in tests. Delete when done."""
    bucket_name = 'test-bucket-{uuid}'.format(uuid=uuid.uuid1())
    yield bucket_name
    delete_bucket(bucket_name, force=True)


@pytest.fixture(scope='function')
def deletable_bucket() -> str:
    """Create a deletable bucket and return its name."""
    bucket_name = 'delete-test-{uuid}'.format(uuid=uuid.uuid1())
    create_bucket(
        storage_bucket_name=bucket_name,
        location='EU',
    )
    return bucket_name


@pytest.fixture(scope='function')
def bucket_and_deletable_file(existing_bucket):
    """Create a deletable file and return its name."""
    filename = 'delete-test-{uuid}'.format(uuid=uuid.uuid1())
    upload_file(b'data', existing_bucket, filename)
    yield (existing_bucket, filename)


@pytest.fixture(scope='module')
def bucket_with_files(existing_bucket):
    """Create files in our test bucket for listing."""
    paths = {'path1/', 'path2/'}
    files = {uuid.uuid1().hex for _ in range(10)}
    files.add('test.txt')  # for exact matches
    filenames = {p + f for p in paths for f in files}  # noqa: WPS111

    for filename_create in filenames:
        upload_file(b'a', existing_bucket, filename_create)
    yield existing_bucket
