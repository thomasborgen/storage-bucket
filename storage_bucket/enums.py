from enum import Enum


class Platform(str, Enum):  # noqa: WPS600
    """All our platform types."""

    gcp = 'google_cloud_platform'
    aws = 'aws'
    azure = 'azure'
