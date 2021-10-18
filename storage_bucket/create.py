from attr import dataclass
from google.cloud.storage import Bucket, Client
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class CreateBucket(object):
    """Create a gcp storage bucket."""

    get_client = GetClient()
    _bucket = Bucket

    def __call__(
        self,
        storage_bucket_name: str,
        location: str,
        storage_class: str = 'STANDARD',
    ) -> Bucket:
        """List the storage bucket files."""
        client = self.get_client()

        return self._create_bucket(
            client=client,
            name=storage_bucket_name,
            storage_class=storage_class,
            location=location,
        )

    def _create_bucket(
        self,
        *,
        client: Client,
        name: str,
        storage_class: str,
        location: str,
    ) -> Bucket:
        bucket = Bucket(client, name=name)
        bucket.storage_class = storage_class
        return client.create_bucket(bucket, location=location)


def create_bucket(
    *,
    storage_bucket_name: str,
    location: str,
    storage_class: str = 'STANDARD',
) -> Bucket:
    """Create bucket but return bucket instead of Modal.

    Raise exception when Modal is in failure state.
    """
    return CreateBucket()(
        storage_bucket_name=storage_bucket_name,
        location=location,
        storage_class=storage_class,
    )
