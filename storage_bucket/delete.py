from attr import dataclass
from google.cloud.storage import Bucket
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class DeleteBucket(object):
    """Delete a gcp storage bucket."""

    get_bucket = GetBucket()

    def __call__(
        self,
        *,
        storage_bucket_name: str,
        force: bool = False,
        **kwargs,
    ) -> None:
        """Delete bucket."""
        bucket = self.get_bucket(
            storage_bucket_name=storage_bucket_name,
        )
        bucket.delete(force=force, **kwargs)


def delete_bucket(
    *,
    storage_bucket_name: str,
    force: bool = False,
    **kwargs,
) -> None:
    """Delete bucket. Returns None on Success.

    Raise exception when Modal is in failure state.
    """
    return DeleteBucket()(
        storage_bucket_name=storage_bucket_name,
        force=force,
        **kwargs,
    )
