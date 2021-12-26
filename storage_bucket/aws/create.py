from storage_bucket.aws.schema import AWSCreateBucket
from storage_bucket.enums import Platform
from storage_bucket.registries import register_create_bucket
from storage_bucket.aws.client import aws_get_client


@register_create_bucket(platform=Platform.aws)
def aws_create_bucket(
    create_params: AWSCreateBucket,
) -> int:
    """Create a gcp storage bucket."""
    print("in aws create bucket")
    client = aws_get_client()

    return 1
