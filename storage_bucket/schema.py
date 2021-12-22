from attr import dataclass



@dataclass
class BaseCreateBucket(object):
    """Base shared create bucket parameters."""

    name: str
