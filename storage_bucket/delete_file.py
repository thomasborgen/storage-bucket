from attr import dataclass
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class DeleteFile(object):
    """
    Deletes a google cloud storage bucket file.

    .. versionadded:: 0.2.0

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name of the file to delete
    :type filename: str

    :param generation: ID of the generation(version) of the file to delete
    :type generation: int

    :param timout: The amount of time, in seconds, to wait for the server
    response.

    :return: Result[None, Exception]
    """

    get_bucket = GetBucket()

    def __call__(
        self,
        storage_bucket_name: str,
        filename: str,
        **kwargs,
    ) -> None:
        """Delete storage bucket file."""
        bucket = self.get_bucket(storage_bucket_name=storage_bucket_name)

        bucket.delete_blob(
            filename,
            **kwargs,
        )


def delete_file(
    storage_bucket_name: str,
    filename: str,
    **kwargs,
) -> None:
    """Delete file with DeleteFile but raise exception on failure."""
    DeleteFile()(
        storage_bucket_name=storage_bucket_name,
        filename=filename,
        **kwargs,
    )
