from attr import dataclass
from google.cloud.storage import Bucket
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class GetBucket(object):
    """Get a GCP storage bucket."""

    get_client = GetClient()

    def __call__(
        self,
        *,
        storage_bucket_name: str,
        **kwargs,
    ) -> Bucket:
        """Get the storage bucket."""
        client = self.get_client()

        return client.get_bucket(storage_bucket_name, **kwargs)


def get_bucket(
    storage_bucket_name: str,
    **kwargs,
) -> Bucket:
    """Run GetBucket."""
    return GetBucket()(
        storage_bucket_name=storage_bucket_name,
        **kwargs,
    )
