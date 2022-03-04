# File/blob operations

## Download

```python
from storage_bucket import download_file

download_file('bucket', 'filename')
```

## Upload

```python
from storage_bucket import upload_file

upload_file(b'data', 'bucket_name', 'filename')
```

## List

```python
from storage_bucket import list_files

list_files('bucket')

list_files('bucket', 'foldername/')
```

## Delete

```python
from storage_bucket import delete_file

delete_file('bucketname', 'filename')
```

# Bucket operations

## Create Bucket

```python
from storage_bucket import create_bucket

create_bucket('bucket-name', 'EU', 'STANDARD')
```

## Delete Bucket

```python
from storage_bucket import delete_bucket

delete_bucket('bucket-name')
```

## List Buckets

```python
from storage_bucket import list_buckets, list_bucket_names

buckets2 = list_buckets()
bucket_names2 = list_bucket_names(buckets2)
```
