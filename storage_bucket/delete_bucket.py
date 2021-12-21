from attr import dataclass

from storage_bucket.enums import Platform
from storage_bucket.registries import get_delete_bucket


@dataclass
class BaseDeleteBucket(object):
    """Base shared create bucket parameters."""

    name: str


def delete_bucket(
    *,
    platform: Platform,
    delete_params: BaseDeleteBucket,
) -> None:
    """Get correct create bucket function and run it."""
    return get_delete_bucket(platform)(delete_params=delete_params)


"""

def temp():
    bucket = self.get_bucket(
        storage_bucket_name=storage_bucket_name,
    )
    bucket.delete(force=force, **kwargs)
"""
