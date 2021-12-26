from typing import TYPE_CHECKING, Any, Literal, NoReturn, Union, overload

from storage_bucket.aws.schema import AWSCreateBucket
from storage_bucket.enums import Platform
from storage_bucket.gcp.schema import GCPCreateBucket
from storage_bucket.registries import get_create_bucket

if TYPE_CHECKING:
    from google.cloud.storage.bucket import Bucket


@overload
def create_bucket(
    *,
    platform: Literal[Platform.gcp],
    create_params: GCPCreateBucket,
) -> 'Bucket':
    """Return strings when platform is gcp."""

@overload
def create_bucket(
    *,
    platform: Literal[Platform.aws],
    create_params: AWSCreateBucket,
) -> int:
    """No good return if create_params is not GCPCreateBucket."""


def create_bucket(
    *,
    platform: Platform,
    create_params: Any,
) -> Union['Bucket', int]:
    """Get correct create bucket function and run it."""
    return get_create_bucket(platform)(create_params=create_params)
