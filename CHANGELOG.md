# Changelog

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |

## Latest Changes



## 4.0.0

### Breaking

* Drop support for python 3.6 - 3.8

### Feature

* Add py.typed file to mark that this library is typed.

### Internal

* Run CI for python 3.9, 3.10, 3.11, 3.12
* Use `uv` instead of `poetry`

## 3.0.0

Remove the callable classes. After we stopped using `returns` they weren't really doing anything. Removing this also removes about half the codebase and makes developing new features easier.

### Breaking

* The Callable class `GetClient` is removed.
* The Callable class `GetBucket` is removed.
* The Callable class `CreateBucket` is removed.
* The Callable class `DeleteBucket` is removed.
* The Callable class `DeleteFile` is removed.
* The Callable class `DownloadFile` is removed.
* The Callable class `ListBuckets` is removed.
* The Callable class `ListFiles` is removed.
* The Callable class `UploadFile` is removed.

### Features

* Can now import directly from `storage_bucket`. Before: `from storage_bucket.download_file import download_file` -> `from storage_bucket import download_file`


### Docs

* Examples in docs now import functions directly from `storage_bucket`
* Removes anything related to returns from docs (48)[https://github.com/thomasborgen/storage-bucket/issues/48]

## 2.0.0 - Return to life before `returns`

This change has been on my mind a while. Using Returns library and especially wanting to use its latest releases creates a dependency hell since every release is breaking. We don't really need it so until its mature enough, lets stop using it.

### Breaking changes

* Remove `returns` dependency
  * One can no longer use `.map`, `.bind`, `.failure` etc after calling the Callable objects like `DeleteFile()().bind(...)`.
  * Instead use the normal snake_case functions like: `delete_file()`

### Fixes

* Test workflows in github are now working again after some key changes.
