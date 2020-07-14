from attr import dataclass
from google.cloud.storage import Bucket
from returns.curry import partial
from returns.functions import raise_exception
from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class DeleteBucket(object):
    """Delete a gcp storage bucket."""

    get_bucket = GetBucket()

    def __call__(
        self,
        storage_bucket_name: str,
        force: bool = False,
        **kwargs,
    ) -> ResultE[None]:
        """Delete bucket."""
        return flow(
            storage_bucket_name,
            self.get_bucket,
            bind(partial(self._delete, force=force, **kwargs)),
        )

    @safe
    def _delete(self, bucket: Bucket, force: bool, **kwargs) -> None:
        # This raises various exceptions.
        bucket.delete(force=force, **kwargs)


def delete_bucket(
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
    ).alt(
        raise_exception,
    ).unwrap()
