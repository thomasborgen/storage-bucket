from typing import Optional, Set

from attr import dataclass
from google.cloud.storage import Blob
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

        return set(client.list_blobs(storage_bucket_name, prefix=prefix))


def list_files(
    *,
    storage_bucket_name: str,
    prefix: Optional[str] = None,
) -> Set[Blob]:
    """Run ListFiles."""
    return ListFiles()(
        storage_bucket_name=storage_bucket_name,
        prefix=prefix,
    )
