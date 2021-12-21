from storage_bucket.delete_bucket import BaseDeleteBucket
from storage_bucket.enums import Platform
from storage_bucket.registries import register_delete_bucket


@register_delete_bucket(platform=Platform.gcp)
def gcp_delete_bucket(delete_params: BaseDeleteBucket):
    """Delete a gcp bucket."""
    print('deleting gcp bucket')
