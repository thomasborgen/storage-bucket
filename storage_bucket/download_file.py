# -*- coding: utf-8 -*-

"""Code to safely download storage bucket files."""

from attr import dataclass
from google.cloud.storage import Blob, Bucket, Client
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final


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

    :param encoding: Optional, Encoding to use when decoding bytes, defaults
    to utf-8
    :type encoding: str

    :return: Success/Failure containers
    """

    _client = Client

    @pipeline(ResultE)
    def __call__(
        self,
        storage_bucket_name: str,
        filename: str,
    ) -> ResultE[bytes]:
        """Download storage bucket file."""
        client = self._initialize_client().unwrap()
        bucket = self._get_bucket(client, storage_bucket_name).unwrap()
        blob = self._get_blob(bucket, filename).unwrap()
        return self._get_bytes(blob)

    @safe
    def _initialize_client(self) -> object:
        return self._client()

    @safe
    def _get_bucket(self, client: Client, storage_bucket_name: str) -> object:
        return client.get_bucket(storage_bucket_name)

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
