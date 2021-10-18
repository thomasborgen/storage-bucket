from attr import dataclass
from google.cloud.storage import Client
from typing_extensions import final


@final
@dataclass(frozen=True, slots=True)
class GetClient(object):
    """Get Client. By default uses gcp Client."""

    client = Client

    def __call__(self) -> Client:
        return self.client()


def get_client() -> Client:
    """Get client help function, no CO."""
    return GetClient()()
