from typing import TYPE_CHECKING, Any, Callable

from storage_bucket.enums import Platform

if TYPE_CHECKING:
    from storage_bucket.create_bucket import BaseCreateBucket
    from storage_bucket.delete_bucket import BaseDeleteBucket

create_bucket_register: dict[str, Callable[['BaseCreateBucket'], Any]] = {}


def register_create_bucket(platform: Platform):
    """Register create bucket functions."""
    def wrapper(create_bucket_func):
        create_bucket_register[platform] = create_bucket_func
        return create_bucket_func
    return wrapper


def get_create_bucket(platform: Platform):
    """Get create bucket function based on platform."""
    func = create_bucket_register.get(platform)

    if func is None:
        raise ValueError(
            'No create bucket registered with platform: {platform}'.format(
                platform=platform.value,
            ),
        )

    return func


delete_bucket_register: dict[str, Callable[['BaseDeleteBucket'], None]] = {}


def register_delete_bucket(platform: Platform):
    """Register get delete_bucket functions."""
    def wrapper(delete_bucket_func):
        delete_bucket_register[platform] = delete_bucket_func
        return delete_bucket_func
    return wrapper


def get_delete_bucket(platform: Platform):
    """Get get client function based on platform."""
    func = delete_bucket_register.get(platform)

    if func is None:
        raise ValueError(
            'No delete bucket function registered with platform: {platform}'.format(
                platform=platform.value,
            ),
        )

    return func
