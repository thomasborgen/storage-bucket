[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# Google Cloud Platform Storage Bucket

This package just aims to make life a little bit easier for people who have to work with google cloud storage bucket.


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

# Returns Modal way
downloader = DownloadFile()
downloader(
    'my_bucket',
    'my_file.txt',
).map(
    use_data_for_something,  # send data to this function,
).alt(
    print,  # print error or send a mail or w/e
)

# Normal way, this might throw exception.
my_data = download_file(
    'my_bucket',
    'my_file.txt',
)
print(my_data)
```

## Supported functions

### Downloading

```python
from storage_bucket.download_file import DownloadFile, download_file

DownloadFile()('bucket', 'filename')
download_file('bucket', 'filename')
```

### Uploading
```python
from storage_bucket.upload_file import UploadFile, upload_file

UploadFile()(b'data', 'bucket_name', 'filename')
upload_file(b'data', 'bucket_name', 'filename')
```

### Listing
```python
from storage_bucket.list_files import ListFiles, list_files

ListFiles()('bucket')
list_files('bucket')

ListFiles()('bucket', 'foldername/')
list_files('bucket', 'foldername/')
```


### The use of [Returns](https://github.com/dry-python/returns) library.
  * Just lets us get rid of all exceptions.
  * Lets us chain stuff so everything looks good.
  * Lets you use `DownloadFile()(args...).map(dostuff).alt(dostuffonfailure)`
  * Don't like it? use the matching normal function provided for your convenience.
