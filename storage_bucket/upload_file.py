from attr import dataclass
from google.cloud.storage import Blob, Bucket
from returns.curry import partial
from returns.functions import raise_exception
from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import ResultE, safe
from typing_extensions import final

from storage_bucket.get import GetBucket


@final
@dataclass(frozen=True, slots=True)
class UploadFile(object):
    """
    Uploades contents in file_data to a google cloud storage bucket.

    .. versionadded:: 0.0.1

    :param file_data: contents to upload in bytes
    :type file_data: bytes

    :param bucket_name: Name of the google cloud bucket
    :type bucket_name: str

    :param filename: The name to give the uploaded file
    :type filename: str

    :param content_type: What type of file to create, defaults to text/plain
    :type content_type: str

    :return: Result[None, Exception]
    """

    get_bucket = GetBucket()

    def __call__(
        self,
        file_content: bytes,
        storage_bucket_name: str,
        filename: str,
        **kwargs,
    ) -> ResultE[None]:
        """Download storage bucket file."""
        return flow(
            storage_bucket_name,
            self.get_bucket,
            bind(partial(self._get_blob, filename=filename)),
            bind(partial(
                self._upload_data,
                file_content=file_content,
                **kwargs,
            )),
        )

    @safe
    def _get_blob(
        self, bucket: Bucket, filename: str,
    ) -> object:
        return bucket.blob(filename)

    @safe
    def _upload_data(
        self, blob: Blob, file_content: bytes, **kwargs,
    ) -> None:
        blob.upload_from_string(file_content, **kwargs)


def upload_file(
    file_content: bytes,
    storage_bucket_name: str,
    filename: str,
    content_type: str = 'application/octet-stream',
) -> None:
    """Upload file as per usual but raise exception on error."""
    return UploadFile()(
        file_content=file_content,
        storage_bucket_name=storage_bucket_name,
        filename=filename,
        content_type=content_type,
    ).alt(
        raise_exception,
    ).unwrap()
