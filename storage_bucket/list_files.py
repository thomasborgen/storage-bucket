# -*- coding: utf-8 -*-

"""Code to safely list storage bucket files."""

from typing import Optional, Set

from attr import dataclass
from google.cloud.storage import Blob, Client
from returns.functions import raise_exception
from returns.pipeline import pipeline
from returns.result import ResultE, safe
from typing_extensions import final


@final
@dataclass(frozen=True, slots=True)
class ListFiles(object):
    """List all blobs in given storage_bucket."""

    _client = Client

    @pipeline(ResultE)
    def __call__(
        self,
        storage_bucket_name: str,
        prefix: Optional[str] = None,
    ) -> ResultE[Set[Blob]]:
        """List the storage bucket files."""
        client = self._initialize_client().unwrap()  # type: ignore
        return self._list_blobs(
            client,
            storage_bucket_name,
            prefix,
        )

    @safe
    def _list_blobs(
        self,
        client: Client,
        storage_bucket_name: str,
        prefix: Optional[str] = None,
    ) -> Set[Blob]:
        return set(client.list_blobs(storage_bucket_name, prefix=prefix))

    @safe
    def _initialize_client(self) -> Client:
        return self._client()


def list_files(
    storage_bucket_name: str,
    prefix: Optional[str] = None,
) -> Set[Blob]:
    """Download file as per usual but raise exception on error."""
    return ListFiles()(
        storage_bucket_name,
        prefix,
    ).alt(
        raise_exception,
    ).unwrap()
