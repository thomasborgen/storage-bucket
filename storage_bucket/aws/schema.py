from typing import Literal, Union

from storage_bucket.schema import BaseCreateBucket


class AWSCreateBucket(BaseCreateBucket):
    """Google Cloud Platform create bucket parameters."""

    storage_class: Union[Literal['STANDARD'], Literal['TEST']]
    location: str
