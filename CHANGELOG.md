# Changelog

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |

## Latest Changes

### Docs

    * Removes anything related to returns from docs (48)[https://github.com/thomasborgen/storage-bucket/issues/48]

## 2.0.0 - Return to life before `returns`

This change has been on my mind a while. Using Returns library and especially wanting to use its latest releases creates a dependency hell since every release is breaking. We don't really need it so until its mature enough, lets stop using it.

### Breaking changes

* Remove `returns` dependency
  * One can no longer use `.map`, `.bind`, `.failure` etc after calling the Callable objects like `DeleteFile()().bind(...)`.
  * Instead use the normal snake_case functions like: `delete_file()`

### Fixes

* Test workflows in github are now working again after some key changes.
