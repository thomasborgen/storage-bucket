from google.cloud.storage import Bucket

from storage_bucket.client import get_client


def create_bucket(
    *,
    storage_bucket_name: str,
    location: str,
    storage_class: str = 'STANDARD',
) -> Bucket:
    """Create storage bucket."""
    client = get_client()

    bucket = Bucket(client, name=storage_bucket_name)
    bucket.storage_class = storage_class
    return client.create_bucket(bucket, location=location)
