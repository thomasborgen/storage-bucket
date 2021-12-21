from google.cloud.storage.client import Client


def aws_get_client() -> Client:
    """Get AWS Client."""
    return Client()
