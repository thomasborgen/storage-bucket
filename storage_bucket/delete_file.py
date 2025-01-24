from storage_bucket.bucket import get_bucket


def delete_file(
    storage_bucket_name: str,
    filename: str,
    **kwargs: dict[str, str],
) -> None:
    """Delete a file."""
    bucket = get_bucket(storage_bucket_name=storage_bucket_name)

    bucket.delete_blob(
        filename,
        **kwargs,
    )
