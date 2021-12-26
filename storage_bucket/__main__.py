from storage_bucket.aws.schema import AWSCreateBucket
from storage_bucket.delete_bucket import BaseDeleteBucket, delete_bucket
from storage_bucket.create_bucket import create_bucket
from storage_bucket.enums import Platform
from storage_bucket.gcp.schema import GCPCreateBucket

test = create_bucket(
    platform=Platform.gcp,
    create_params=GCPCreateBucket(
        name='test',
        location='norway',
        storage_class='STANDARD',
    ),
)

bob = create_bucket(
    platform=Platform.aws,
    create_params=AWSCreateBucket(name='bob'),
)

bob = create_bucket(
    platform=Platform.aws,
    create_params=AWSCreateBucket(name='bob'),
)

delete_gcp = delete_bucket(
    platform=Platform.gcp,
    delete_params=BaseDeleteBucket(name='bucket'),
)

delete_aws = delete_bucket(
    platform=Platform.aws,
    delete_params=BaseDeleteBucket(name='s3'),
)
