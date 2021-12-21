from typing import Literal, Union

from storage_bucket.create_bucket import BaseCreateBucket
from storage_bucket.enums import Platform
from storage_bucket.registries import register_create_bucket
from storage_bucket.aws.client import aws_get_client


class AWSCreateBucket(BaseCreateBucket):
    """Google Cloud Platform create bucket parameters."""

    storage_class: Union[Literal['STANDARD'], Literal['TEST']]
    location: str


@register_create_bucket(platform=Platform.aws)
def aws_create_bucket(
    create_params: AWSCreateBucket,
) -> int:
    """Create a gcp storage bucket."""
    client = aws_get_client()
    print("in aws create bucket")

    return 1
