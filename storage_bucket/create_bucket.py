from typing import TYPE_CHECKING, Any, Literal, Union, overload

from attr import dataclass

from storage_bucket.enums import Platform
from storage_bucket.registries import get_create_bucket

if TYPE_CHECKING:
    from google.cloud.storage.bucket import Bucket


@dataclass
class BaseCreateBucket(object):
    """Base shared create bucket parameters."""

    name: str


@overload
def create_bucket(
    *,
    platform: Literal[Platform.gcp],
    create_params: BaseCreateBucket,
) -> 'Bucket':
    """Return strings when platform is gcp."""


@overload
def create_bucket(
    *,
    platform: Literal[Platform.aws],
    create_params: BaseCreateBucket,
) -> int:
    """Return int when platform is aws."""


@overload
def create_bucket(
    *,
    platform: Platform,
    create_params: BaseCreateBucket,
) -> Any:
    """Not sure what we return if platform is not provided."""


def create_bucket(
    *,
    platform: Platform,
    create_params: BaseCreateBucket,
) -> Union[int, str, Any]:
    """Get correct create bucket function and run it."""
    return get_create_bucket(platform)(create_params=create_params)
