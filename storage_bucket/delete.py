# -*- coding: utf-8 -*-

"""Code to safely delete a storage bucket."""

from typing import Optional, Tuple, Union

from attr import dataclass
from google.cloud.storage import Bucket, Client
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.constants import DEFAULT_TIMEOUT

TIMEOUT_TYPE = Optional[Union[float, Tuple[float, float]]]


@final
@dataclass(frozen=True, slots=True)
class DeleteBucket(object):
    """Create a gcp storage bucket."""

    _client = Client

    @pipeline(ResultE)
    def __call__(
        self,
        storage_bucket_name: str,
        force: bool = False,
        timeout: TIMEOUT_TYPE = DEFAULT_TIMEOUT,
    ) -> ResultE[None]:
        """List the storage bucket files."""
        client = self._initialize_client().unwrap()  # type: ignore

        bucket = self._get_bucket(  # type: ignore
            client, storage_bucket_name,
        ).unwrap()

        return self._delete(bucket, force, timeout)

    @safe
    def _get_bucket(self, client: Client, name: str) -> Bucket:
        return client.get_bucket(name)

    @safe
    def _delete(
        self,
        bucket: Bucket,
        force: bool,
        timeout: TIMEOUT_TYPE,
    ) -> None:
        # This raises various exceptions.
        bucket.delete(force=force, timeout=timeout)

    @safe
    def _initialize_client(self) -> Client:
        return self._client()


def delete_bucket(
    storage_bucket_name: str,
    force: bool = False,
    timeout: TIMEOUT_TYPE = DEFAULT_TIMEOUT,
) -> None:
    """Delete bucket. Returns None on Success.

    Raise exception when Modal is in failure state.
    """
    return DeleteBucket()(
        storage_bucket_name=storage_bucket_name,
        force=force,
        timeout=timeout,
    ).alt(
        raise_exception,
    ).unwrap()
