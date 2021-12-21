from storage_bucket.delete_bucket import BaseDeleteBucket
from storage_bucket.enums import Platform
from storage_bucket.registries import register_delete_bucket


@register_delete_bucket(platform=Platform.aws)
def aws_delete_bucket(delete_params: BaseDeleteBucket):
    """Delete an aws bucket."""
    print('deleting aws bucket')
