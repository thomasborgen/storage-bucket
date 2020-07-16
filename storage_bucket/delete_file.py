from functools import partial

from attr import dataclass
from google.cloud.storage import Bucket
from returns.functions import raise_exception
from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import ResultE, safe
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

    _get_bucket = GetBucket()

    def __call__(
        self,
        storage_bucket_name: str,
        filename: str,
        **kwargs,
    ) -> ResultE[None]:
        """Delete storage bucket file."""
        return flow(
            storage_bucket_name,
            self._get_bucket,
            bind(partial(
                self._delete_file,
                filename=filename,
                **kwargs,
            )),
        )

    @safe
    def _delete_file(
        self,
        bucket: Bucket,
        filename: str,
        **kwargs,
    ) -> None:
        bucket.delete_blob(filename, **kwargs)


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
    ).alt(
        raise_exception,
    ).unwrap()
