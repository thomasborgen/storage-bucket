# -*- coding: utf-8 -*-

"""Code to safely list storage buckets."""
from typing import Iterator, Optional, Set, Union

from attr import dataclass
from google.cloud.storage import Bucket, Client
from returns.functions import raise_exception
from returns.result import safe
from typing_extensions import final


@final
@dataclass(frozen=True, slots=True)
class ListBuckets(object):
    """List storage buckets.

    .. code:: python

      >>> from returns.pipeline import is_successful
      >>> assert ListBuckets()()
      >>> assert is_successful(ListBuckets()(prefix='test'))
    """

    _client = Client

    @safe
    def __call__(  # noqa: WPS211
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
        client = self._initialize_client().alt(  # type: ignore
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

    @safe
    def _initialize_client(self) -> Client:
        return self._client()


def list_buckets(  # noqa: WPS211
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
