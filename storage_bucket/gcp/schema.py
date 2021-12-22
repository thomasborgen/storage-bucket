from typing import Literal, Union

from attr import dataclass

from storage_bucket.schema import BaseCreateBucket


@dataclass
class GCPCreateBucket(BaseCreateBucket):
    """Google Cloud Platform create bucket parameters."""

    storage_class: Union[Literal['STANDARD'], Literal['TEST']]
    location: str
