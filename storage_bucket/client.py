from google.cloud.storage import Client


def get_client() -> Client:
    """Run GetClient."""
    return Client()
