"""
Run these imports so that the functions are registered correctly
"""

from storage_bucket.gcp import *
from storage_bucket.aws import *

from storage_bucket.create_bucket import create_bucket
from storage_bucket.delete_bucket import delete_bucket

__all__ = ['create_bucket', 'delete_bucket']
