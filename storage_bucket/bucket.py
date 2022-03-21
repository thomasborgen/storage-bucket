from google.cloud.storage import Bucket

from storage_bucket.client import get_client


def get_bucket(
    storage_bucket_name: str,
    **kwargs,
) -> Bucket:
    """Get a storage bucket."""
    client = get_client()
    return client.get_bucket(storage_bucket_name, **kwargs)
