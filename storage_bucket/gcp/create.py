from google.cloud.storage.bucket import Bucket

from storage_bucket.enums import Platform
from storage_bucket.gcp.client import gcp_get_client
from storage_bucket.gcp.schema import GCPCreateBucket
from storage_bucket.registries import register_create_bucket


@register_create_bucket(platform=Platform.gcp)
def gcp_create_bucket(
    create_params: GCPCreateBucket,
) -> Bucket:
    """Create a gcp storage bucket."""
    print("in gcp create bucket")

    client = gcp_get_client()
    bucket = Bucket(client, name=create_params.name)
    bucket.storage_class = create_params.storage_class
    return bucket

    """
    return client.create_bucket(
        bucket,
        location=create_params.location,
    )
    """
