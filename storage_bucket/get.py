from attr import dataclass
from google.cloud.storage import Bucket, Client
from returns.curry import partial
from returns.functions import raise_exception
from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class GetBucket(object):
    """Get a GCP storage bucket."""

    get_client = GetClient()

    def __call__(
        self,
        storage_bucket_name: str,
        **kwargs,
    ) -> ResultE[Bucket]:
        """Get the storage bucket."""
        return flow(
            self.get_client(),
            bind(partial(
                self._get_bucket,
                storage_bucket_name=storage_bucket_name,
                **kwargs,
            )),
        )

    @safe
    def _get_bucket(
        self,
        client: Client,
        storage_bucket_name: str,
        **kwargs,
    ) -> Bucket:
        return client.get_bucket(storage_bucket_name, **kwargs)


def get_bucket(
    storage_bucket_name: str,
    **kwargs,
) -> Bucket:
    """Get bucket but return bucket instead of Modal.

    Raise exception when Modal is in failure state.
    """
    return GetBucket()(
        storage_bucket_name=storage_bucket_name,
        **kwargs,
    ).alt(
        raise_exception,
    ).unwrap()
