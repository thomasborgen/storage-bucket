from storage_bucket.bucket import get_bucket


def download_file(
    *,
    storage_bucket_name: str,
    filename: str,
) -> bytes:
    """
    Download a google cloud storage bucket file.

    .. versionadded:: 0.1.0

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name of the file to download
    :type filename: str

    :return: bytes
    """
    bucket = get_bucket(storage_bucket_name=storage_bucket_name)

    blob = bucket.blob(filename)

    return blob.download_as_bytes()
