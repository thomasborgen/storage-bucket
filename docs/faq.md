# FAQ

## How is it different from the google-cloud-storage library designed and maintained by Google?

This library is built on top of [google-cloud-storage](google-cloud-storage). `storage-bucket` library allows to work in functional style and abstracts away common use-cases which bloats code with boileraplate. It enables smooth integration with [`returns`](https://github.com/dry-python/returns) library functional style and powered by it.

## What if there isn't feature I need?

Feel free to submit ticket with explanation of what is missing and possible use-case how you will use it.

At the moment, `storage-bucket` doesn't support all scenarios exising in `google-cloud-storage` but we are actively developing to make 100% compatability.
