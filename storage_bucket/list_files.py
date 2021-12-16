from typing import Optional, Set

from attr import dataclass
from google.cloud.storage import Blob, Client
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class ListFiles(object):
    """List all blobs in given storage_bucket."""

    get_client = GetClient()

    def __call__(
        self,
        *,
        storage_bucket_name: str,
        prefix: Optional[str] = None,
    ) -> Set[Blob]:
        """List the storage bucket files."""
        client = self.get_client()

        return self._list_blobs(
            client=client,
            storage_bucket_name=storage_bucket_name,
            prefix=prefix,
        )

    def _list_blobs(
        self,
        client: Client,
        storage_bucket_name: str,
        prefix: Optional[str] = None,
    ) -> Set[Blob]:
        return set(client.list_blobs(storage_bucket_name, prefix=prefix))


def list_files(
    *,
    storage_bucket_name: str,
    prefix: Optional[str] = None,
) -> Set[Blob]:
    """Download file as per usual but raise exception on error."""
    return ListFiles()(
        storage_bucket_name=storage_bucket_name,
        prefix=prefix,
    )
