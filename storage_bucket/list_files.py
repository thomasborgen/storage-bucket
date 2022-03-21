from typing import Optional, Set

from google.cloud.storage import Blob

from storage_bucket.client import get_client


def list_files(
    *,
    storage_bucket_name: str,
    prefix: Optional[str] = None,
) -> Set[Blob]:
    """List all files in a given storage bucket."""
    client = get_client()

    return set(client.list_blobs(storage_bucket_name, prefix=prefix))
