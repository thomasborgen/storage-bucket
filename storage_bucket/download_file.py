# -*- coding: utf-8 -*-

"""Code to safely download storage bucket files."""

from attr import dataclass
from google.cloud.storage import Blob, Bucket
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class DownloadFile(object):
    """
    Downloades a google cloud storage bucket file.

    .. versionadded:: 0.1.0

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name of the file to download
    :type filename: str

    :return: Result[bytes, Exception]
    """

    _get_bucket = GetBucket()

    @pipeline(ResultE)
    def __call__(
        self,
        storage_bucket_name: str,
        filename: str,
    ) -> ResultE[bytes]:
        """Download storage bucket file."""
        bucket = self._get_bucket(storage_bucket_name).unwrap()
        blob = self._get_blob(bucket, filename).unwrap()
        return self._get_bytes(blob)

    @safe
    def _get_blob(self, bucket: Bucket, filename: str) -> object:
        return bucket.blob(filename)

    @safe
    def _get_bytes(self, blob: Blob) -> bytes:
        return blob.download_as_string()


def download_file(
    storage_bucket_name: str,
    filename: str,
) -> bytes:
    """Download file as per usual but raise exception on error."""
    return DownloadFile()(
        storage_bucket_name,
        filename,
    ).alt(
        raise_exception,
    ).unwrap()
