from storage_bucket.bucket import get_bucket


def upload_file(
    *,
    file_content: bytes,
    storage_bucket_name: str,
    filename: str,
    content_type: str = 'application/octet-stream',
    **kwargs: dict,
) -> None:
    """
    Upload content of file_data to a google cloud storage bucket.

    .. versionadded:: 0.0.1

    :param file_data: contents to upload in bytes
    :type file_data: bytes

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name to give the uploaded file
    :type filename: str

    :param content_type: What type of file to create, defaults to text/plain
    :type content_type: str

    :return: None
    """
    bucket = get_bucket(storage_bucket_name=storage_bucket_name)

    blob = bucket.blob(filename)
    blob.upload_from_string(
        file_content,
        content_type=content_type,
        **kwargs,
    )
