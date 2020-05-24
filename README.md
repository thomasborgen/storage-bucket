[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# Google Cloud Platform Storage Bucket

This package just aims to make life a little bit easier for people who have to work with google cloud storage bucket.

* [Quickstart](#quickstart)
* [File/Blob operations](#file/blob-operations)
  * [Download](#download)
  * [Upload](#upload)
  * [List](#list)
  * [Delete](#delete)
* [Bucket operations](#bucket-operations)
  * [Create](#create-bucket)
  * [Delete](#delete-bucket)
  * [List Buckets](#list-buckets)


## Quickstart:

1. get the package
  * `pip install storage-bucket`
2. Download your keyfile and save it as key.json and point to it with env var:
  * `gcloud iam service-accounts keys create key.json --iam-account your_service_account@your_project.iam.gserviceaccount.com`
  * `export GOOGLE_APPLICATION_CREDENTIALS='key.json'`
3. Run some code:


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


# Returns Modal way
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


### The use of [Returns](https://github.com/dry-python/returns) library.
  * Lets us get rid of all exceptions.
  * Lets us chain stuff so everything looks good.
  * Lets you use `DownloadFile()(args...).map(dostuff).alt(dostuffonfailure)`
  * Don't like it? use the matching normal function provided for your convenience.
