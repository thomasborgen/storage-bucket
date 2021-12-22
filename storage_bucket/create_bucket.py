from typing import TYPE_CHECKING, Literal, NoReturn, Union, overload

from storage_bucket.aws.schema import AWSCreateBucket
from storage_bucket.enums import Platform
from storage_bucket.gcp.schema import GCPCreateBucket
from storage_bucket.registries import get_create_bucket
from storage_bucket.schema import BaseCreateBucket

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
) -> NoReturn:
    """No good return if create_params is not GCPCreateBucket."""


@overload
def create_bucket(
    *,
    platform: Platform,
    create_params: BaseCreateBucket,
) -> NoReturn:
    """No good return if create_params is not GCPCreateBucket."""


def create_bucket(
    *,
    platform: Platform,
    create_params: BaseCreateBucket,
) -> Union['Bucket', int]:
    """Get correct create bucket function and run it."""
    return get_create_bucket(platform)(create_params=create_params)
