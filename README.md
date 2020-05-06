# Google Cloud Platform Storage Bucket EaseyBreezey

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

### The use of [Returns](https://github.com/dry-python/returns) library.
  * Just lets us get rid of all exceptions.
  * Lets us chain stuff so everything looks good.
  * Lets you use `DownloadFile()(args...).bind(dostuff).alt(dostuffonfailure)`
  * Don't like it? use the matching normal function provided for your convenience.


