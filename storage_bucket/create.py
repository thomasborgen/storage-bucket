from attr import dataclass
from google.cloud.storage import Bucket
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class CreateBucket(object):
    """Create a gcp storage bucket."""

    get_client = GetClient()

    def __call__(
        self,
        storage_bucket_name: str,
        location: str,
        storage_class: str = 'STANDARD',
    ) -> Bucket:
        """List the storage bucket files."""
        client = self.get_client()

        bucket = Bucket(client, name=storage_bucket_name)
        bucket.storage_class = storage_class
        return client.create_bucket(bucket, location=location)


def create_bucket(
    *,
    storage_bucket_name: str,
    location: str,
    storage_class: str = 'STANDARD',
) -> Bucket:
    """Run CreateBucket."""
    return CreateBucket()(
        storage_bucket_name=storage_bucket_name,
        location=location,
        storage_class=storage_class,
    )
