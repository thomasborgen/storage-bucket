```python
from storage_bucket.download_file import DownloadFile, download_file


def use_data_for_something(data):
    print(data)


# Normal way, this might throw exception... handle them yourself.
my_data = download_file(
    'my_bucket',
    'my_file.txt',
)
use_data_for_something(my_data)


# Functional way
# this will _only_ call use_data_for_something when data is successfully downloaded.
# so its completely safe.
DownloadFile()(
    'my_bucket',
    'my_file.txt',
).map(
    use_data_for_something,  # send data to this function,
)

```

## File/blob operations

### Download

```python
from storage_bucket.download_file import DownloadFile, download_file

DownloadFile()('bucket', 'filename')
download_file('bucket', 'filename')
```

### Upload
```python
from storage_bucket.upload_file import UploadFile, upload_file

UploadFile()(b'data', 'bucket_name', 'filename')
upload_file(b'data', 'bucket_name', 'filename')
```

### List
```python
from storage_bucket.list_files import ListFiles, list_files

ListFiles()('bucket')
list_files('bucket')

ListFiles()('bucket', 'foldername/')
list_files('bucket', 'foldername/')
```

### Delete
```python
from storage_bucket.delete_file import DeleteFile, delete_file

DeleteFile()('bucketname', 'filename')
delete_file('bucketname', 'filename')
```

## Bucket operations

### Create Bucket
```python
from storage_bucket.create import CreateBucket, create_bucket

CreateBucket()('bucket-name', 'EU', 'STANDARD')
create_bucket('bucket-name', 'EU', 'STANDARD')

```

### Delete Bucket
```python
from storage_bucket.delete import DeleteBucket, delete_bucket

DeleteBucket()('bucket-name')
delete_bucket('bucket-name')

```

### List Buckets
```python
from storage_bucket.list import ListBuckets, list_buckets, list_bucket_names

buckets = ListBuckets()()
bucket_names = list_bucket_names(buckets.unwrap())

buckets2 = list_buckets()
bucket_names2 = list_bucket_names(buckets2)
```