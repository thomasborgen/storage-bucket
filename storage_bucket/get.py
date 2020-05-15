# -*- coding: utf-8 -*-

"""Code to safely get storage bucket."""

from typing import Optional, Tuple, Union

from attr import dataclass
from google.cloud.storage import Bucket, Client
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final


@final
@dataclass(frozen=True, slots=True)
class GetBucket(object):
    """Get a GCP storage bucket."""

    _client = Client

    @pipeline(ResultE)
    def __call__(  # noqa: WPS234
        self,
        storage_bucket_name: str,
        timeout: Optional[Union[float, Tuple[float, float]]] = 60,
    ) -> ResultE[Bucket]:
        """Get the storage bucket."""
        client = self._initialize_client().unwrap()  # type: ignore
        return self._get_bucket(  # type: ignore
            client,
            storage_bucket_name,
            timeout,
        )

    @safe
    def _get_bucket(  # noqa: WPS234
        self,
        client: Client,
        bucket_name: str,
        timeout: Optional[Union[float, Tuple[float, float]]],
    ) -> Bucket:
        return client.get_bucket(bucket_name)

    @safe
    def _initialize_client(self) -> Client:
        return self._client()


def get_bucket(
    storage_bucket_name: str,
) -> Bucket:
    """Get bucket but return bucket instead of Modal.

    Raise exception when Modal is in failure state.
    """
    return GetBucket()(
        storage_bucket_name=storage_bucket_name,
    ).alt(
        raise_exception,
    ).unwrap()
