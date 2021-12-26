from google.cloud.storage.client import Client


def gcp_get_client() -> Client:
    """Get GCP Client"""
    return Client()
