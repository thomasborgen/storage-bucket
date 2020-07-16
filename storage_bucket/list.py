from typing import Callable, Iterator, Optional, Set, Union

from attr import dataclass
from google.cloud.storage import Bucket
from returns.functions import raise_exception
from returns.result import safe
from typing_extensions import final

from storage_bucket.client import GetClient


@final
@dataclass(frozen=True, slots=True)
class ListBuckets(object):
    """List storage buckets.

    .. code:: python

      >>> from returns.pipeline import is_successful
      >>> assert ListBuckets()()
      >>> assert is_successful(ListBuckets()(prefix='test'))
    """

    get_client: Callable = GetClient()

    @safe
    def __call__(
        self,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        prefix: Optional[str] = None,
        fields: Optional[Set] = None,
        projection: str = 'noAcl',
        project: Optional[str] = None,
        timeout: Union[float, int] = 60,
    ) -> Set[Bucket]:
        """List the storage bucket files."""
        client = self.get_client().alt(
            raise_exception,
        ).unwrap()

        return client.list_buckets(
            max_results=max_results,
            page_token=page_token,
            prefix=prefix,
            fields=fields,
            projection=projection,
            project=project,
            timeout=timeout,
        )


def list_buckets(
    max_results: Optional[int] = None,
    page_token: Optional[str] = None,
    prefix: Optional[str] = None,
    fields: Optional[Set] = None,
    projection: str = 'noAcl',
    project: Optional[str] = None,
    timeout: Union[float, int] = 60,
) -> Bucket:
    """List Buckets, but return Set[Bucket] instead of ResultE[Set[Bucket]].

    Raise exception when Modal is in failure state.
    """
    return ListBuckets()(
        max_results=max_results,
        page_token=page_token,
        prefix=prefix,
        fields=fields,
        projection=projection,
        project=project,
        timeout=timeout,
    ).alt(
        raise_exception,
    ).unwrap()


def list_bucket_names(buckets: Set[Bucket]) -> Iterator[str]:
    """Iterate over Buckets and retrieve their names.

    Raise NoneType Exception when Bucket is None.
    """
    return map(lambda bucket: bucket.name, buckets)
