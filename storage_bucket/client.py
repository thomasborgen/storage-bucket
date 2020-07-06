from attr import dataclass
from google.cloud.storage import Client
from returns.functions import raise_exception
from returns.result import ResultE, safe
from typing_extensions import final


@final
@dataclass(frozen=True, slots=True)
class GetClient(object):
    """Create a gcp storage bucket."""

    client = Client

    @safe
    def __call__(self) -> ResultE[Client]:
        """List the storage bucket files."""
        return self.client()


def get_client() -> Client:
    """Create bucket but return bucket instead of Modal.

    Raise exception when Modal is in failure state.
    """
    return GetClient()().alt(
        raise_exception,
    ).unwrap()
