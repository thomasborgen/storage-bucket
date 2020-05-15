# -*- coding: utf-8 -*-

"""Code to safely upload storage bucket files."""

from attr import dataclass
from google.cloud.storage import Blob, Bucket
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class UploadFile(object):
    """
    Uploades contents in file_data to a google cloud storage bucket.

    .. versionadded:: 0.0.1

    :param file_data: contents to upload in bytes
    :type file_data: bytes

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name to give the uploaded file
    :type filename: str

    :param content_type: What type of file to create, defaults to text/plain
    :type content_type: str

    :return: Result[None, Exception]
    """

    _get_bucket = GetBucket()

    @pipeline(ResultE)
    def __call__(
        self,
        file_data: bytes,
        storage_bucket_name: str,
        filename: str,
        content_type: str = 'application/octet-stream',
    ) -> ResultE[None]:
        """Download storage bucket file."""
        bucket = self._get_bucket(storage_bucket_name).unwrap()
        blob = self._get_blob(bucket, filename).unwrap()
        return self._upload_data(blob, file_data, content_type)

    @safe
    def _get_blob(
        self, bucket: Bucket, filename: str,
    ) -> object:
        return bucket.blob(filename)

    @safe
    def _upload_data(
        self, blob: Blob, file_content: bytes, content_type: str,
    ) -> None:
        blob.upload_from_string(file_content, content_type)


def upload_file(
    file_data: bytes,
    storage_bucket_name: str,
    filename: str,
    content_type: str = 'application/octet-stream',
) -> None:
    """Upload file as per usual but raise exception on error."""
    return UploadFile()(
        file_data,
        storage_bucket_name,
        filename,
        content_type,
    ).alt(
        raise_exception,
    ).unwrap()
