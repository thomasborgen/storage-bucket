## Quickstart

1. get the package
  * `pip install storage-bucket`
2. Download your keyfile and save it as key.json and point to it with env var:
  * `gcloud iam service-accounts keys create key.json --iam-account your_service_account@your_project.iam.gserviceaccount.com`
  * `export GOOGLE_APPLICATION_CREDENTIALS='key.json'`
3. Run some code.

See [Usage](usage.md).
