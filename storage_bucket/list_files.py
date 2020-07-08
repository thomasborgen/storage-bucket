from typing import Optional, Set

from attr import dataclass
from google.cloud.storage import Blob, Client
from returns.curry import partial
from returns.functions import raise_exception
from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class ListFiles(object):
    """List all blobs in given storage_bucket."""

    get_client = GetClient()

    def __call__(
        self,
        storage_bucket_name: str,
        prefix: Optional[str] = None,
    ) -> ResultE[Set[Blob]]:
        """List the storage bucket files."""
        return flow(
            self.get_client(),
            bind(partial(
                self._list_blobs,
                storage_bucket_name=storage_bucket_name,
                prefix=prefix,
            )),
        )

    @safe
    def _list_blobs(
        self,
        client: Client,
        storage_bucket_name: str,
        prefix: Optional[str] = None,
    ) -> Set[Blob]:
        return set(client.list_blobs(storage_bucket_name, prefix=prefix))


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
