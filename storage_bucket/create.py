# -*- coding: utf-8 -*-

"""Code to safely list, download and upload storage bucket files."""

from attr import dataclass
from google.cloud.storage import Bucket, Client
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final


@final
@dataclass(frozen=True, slots=True)
class CreateBucket(object):
    """Create a gcp storage bucket."""

    _client = Client
    _bucket = Bucket

    @pipeline(ResultE)
    def __call__(
        self,
        storage_bucket_name: str,
        location: str,
        storage_class: str = 'STANDARD',
    ) -> ResultE[Bucket]:
        """List the storage bucket files."""
        client = self._initialize_client().unwrap()  # type: ignore
        bucket = self._initialize_bucket(  # type: ignore
            client,
            storage_bucket_name,
            storage_class,
        ).unwrap()

        return self._create_bucket(client, bucket, location)  # type: ignore

    @safe
    def _create_bucket(
        self,
        client: Client,
        bucket: Bucket,
        location: str,
    ) -> Bucket:
        return client.create_bucket(bucket, location=location)

    @safe
    def _initialize_bucket(
        self, client: Client, name: str, storage_class: str,
    ) -> Bucket:
        bucket = Bucket(client, name=name)
        bucket.storage_class = storage_class
        return bucket

    @safe
    def _initialize_client(self) -> Client:
        return self._client()


def create_bucket(
    storage_bucket_name: str,
    location: str,
    storage_class: str = 'STANDARD',
) -> Bucket:
    """Create bucket but return bucket instead of Modal.

    Raise exception when Modal is in failure state.
    """
    return CreateBucket()(
        storage_bucket_name=storage_bucket_name,
        location=location,
        storage_class=storage_class,
    ).alt(
        raise_exception,
    ).unwrap()
