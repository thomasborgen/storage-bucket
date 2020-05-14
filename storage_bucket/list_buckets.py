# -*- coding: utf-8 -*-

"""Code to safely list storage buckets."""
from typing import Optional, Set

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
      >>> assert is_successful(ListBuckets()('test'))
    """

    _client = Client

    @safe
    def __call__(
        self,
        prefix: Optional[str] = None,
        fields: Optional[Set] = None,
        projection: str = 'noAcl',
        project: Optional[str] = None,
    ) -> Set[Bucket]:
        """List the storage bucket files."""
        client = self._initialize_client().alt(  # type: ignore
            raise_exception,
        ).unwrap()

        return client.list_buckets(
            prefix=prefix,
            fields=fields,
            projection=projection,
            project=project,
        )

    @safe
    def _initialize_client(self) -> Client:
        return self._client()


def list_buckets(
    prefix: Optional[str] = None,
    fields: Optional[Set] = None,
    projection: str = 'noAcl',
    project: Optional[str] = None,
) -> Bucket:
    """List Buckets, but return Set[Bucket] instead of ResultE[Set[Bucket]].

    Raise exception when Modal is in failure state.
    """
    return ListBuckets()(
        prefix=prefix,
        fields=fields,
        projection=projection,
        project=project,
    ).alt(
        raise_exception,
    ).unwrap()
