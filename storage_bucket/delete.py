from storage_bucket.bucket import get_bucket


def delete_bucket(
    *,
    storage_bucket_name: str,
    force: bool = False,
    **kwargs,
) -> None:
    """Delete a storage bucket."""
    bucket = get_bucket(
        storage_bucket_name=storage_bucket_name,
    )
    bucket.delete(force=force, **kwargs)
