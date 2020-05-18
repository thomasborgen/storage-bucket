# -*- coding: utf-8 -*-

"""Code to safely download storage bucket files."""
from typing import Optional, Tuple, Union

from attr import dataclass
from returns.functions import raise_exception
from returns.result import safe
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

    @safe
    def __call__(  # noqa: WPS234  fix annotation with a timeout type
        self,
        storage_bucket_name: str,
        filename: str,
        generation: Optional[int] = None,
        timeout: Optional[Union[int, Tuple[int, int]]] = None,
    ) -> None:
        """Delete storage bucket file."""
        bucket = self._get_bucket(storage_bucket_name).alt(
            raise_exception,
        ).unwrap()

        bucket.delete_blob(filename)


def delete_file(
    storage_bucket_name: str,
    filename: str,
    generation: Optional[int] = None,
) -> None:
    """Delete file with DeleteFile but raise exception on failure."""
    DeleteFile()(
        storage_bucket_name=storage_bucket_name,
        filename=filename,
        generation=generation,
    ).alt(
        raise_exception,
    ).unwrap()
