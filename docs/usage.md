# File/blob operations

## Download

```python
from storage_bucket.download_file import download_file

download_file('bucket', 'filename')
```

## Upload

```python
from storage_bucket.upload_file import upload_file

upload_file(b'data', 'bucket_name', 'filename')
```

## List

```python
from storage_bucket.list_files import list_files

list_files('bucket')

list_files('bucket', 'foldername/')
```

## Delete

```python
from storage_bucket.delete_file import delete_file

delete_file('bucketname', 'filename')
```

# Bucket operations

## Create Bucket

```python
from storage_bucket.create import create_bucket

create_bucket('bucket-name', 'EU', 'STANDARD')
```

## Delete Bucket

```python
from storage_bucket.delete import delete_bucket

delete_bucket('bucket-name')
```

## List Buckets

```python
from storage_bucket.list import list_buckets, list_bucket_names

buckets2 = list_buckets()
bucket_names2 = list_bucket_names(buckets2)
```
