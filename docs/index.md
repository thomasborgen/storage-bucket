# Storage Bucket

Makes working with GCP Storage bucket a breeze

___
![test](https://github.com/thomasborgen/storage-bucket/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/thomasborgen/storage-bucket/branch/master/graph/badge.svg)](https://codecov.io/gh/thomasborgen/storage-bucket)
[![Python Version](https://img.shields.io/pypi/pyversions/storage-bucket.svg)](https://pypi.org/project/storage-bucket/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
___

**[Documentation](https://thomasborgen.github.io/storage-bucket/) |
[Source Code](https://github.com/thomasborgen/storage-bucket) |
[Issue Tracker](https://github.com/thomasborgen/storage-bucket/issues)**

The goal of this package is to make it easy to work with GCP Storage Bucket. We felt that using googles package(google-cloud-storage) was a horrible experience and we believe that this package abstracts away the object oriented approach taken by google and introduces a more functional approach.

## Quickstart

Get the package
```sh
pip install storage-bucket
```

Or better with `poetry`
```sh
poetry add storage-bucket
```

Download your keyfile and save it as key.json and point to it with env var:

```sh
gcloud iam service-accounts keys create key.json --iam-account your_service_account@your_project.iam.gserviceaccount.com
```

```sh
export GOOGLE_APPLICATION_CREDENTIALS='key.json'
```


### Download
```python
from storage_bucket import download_file

file_data = download_file('bucket', 'filename')

print(file_data)
```

### Upload
```python
from storage_bucket import upload_file

upload_file(b'data', 'bucket_name', 'filename')
```

### Supported operations - File

`Download`, `Upload`, `List`, `Delete`

### Supported operations - Bucket

`Create`, `Delete`, `List`

### Check [Usage](https://thomasborgen.github.io/storage-bucket/usage).

## Contribution

Like the library and want to help us, check: [contributing](https://thomasborgen.github.io/storage-bucket/contrib/contributing/)
