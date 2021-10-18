from attr import dataclass
from google.cloud.storage import Blob, Bucket
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class DownloadFile(object):
    """
    Downloades a google cloud storage bucket file.

    .. versionadded:: 0.1.0

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name of the file to download
    :type filename: str

    :return: Result[bytes, Exception]
    """

    get_bucket = GetBucket()

    def __call__(
        self,
        *,
        storage_bucket_name: str,
        filename: str,
    ) -> bytes:
        """Download storage bucket file."""
        bucket = self.get_bucket(storage_bucket_name=storage_bucket_name)

        blob = bucket.blob(filename)

        return blob.download_as_string()


def download_file(
    *,
    storage_bucket_name: str,
    filename: str,
) -> bytes:
    """Download file as per usual but raise exception on error."""
    return DownloadFile()(
        storage_bucket_name=storage_bucket_name,
        filename=filename,
    )
