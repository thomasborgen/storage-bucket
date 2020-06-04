# How to contribute

## Dependencies

As a dependency manager we use [poetry](https://github.com/python-poetry/poetry).

To install correct versions of dependencies you would need to do installation via:

```
poetry install
```


## GCP

>You don't need your own gcp project to test this, since pushing to a branch will run tests for you, but this will make your feedback loop much faster.

To get everything set up you should have a gcp project, most people can get a year of usage with a lot of stuff for free and that is sufficient for all testing we're doing in `storage-bucket`.

Get the gcloud cli - [quickstart](https://cloud.google.com/sdk/docs/quickstarts)

Make a service account or [find the default SA for storage bucket](https://cloud.google.com/storage/docs/getting-service-account)

CD into this dir and create a key with:
```
gcloud iam service-accounts keys create key.json --iam-account serviceaccount-name@project-id.iam.gserviceaccount.com
```
replace `serviceaccount-name` and `project-id` with your own values.

This will create the file `key.json` in your working dir.

And thats all you need to get going.


## Tests

We use `pytest`, `flake8` and `mypy` as a quality gate. We follow `wemake_python_styleguide` to enforce quality.

Since storage bucket names must be globally unique, we use a environment variable for the storage bucket name in tests. which means that you must set the env var `STORAGE_BUCKET_NAME` to whatever the name of your bucket is.
>This might be removed in the future.

To run all tests:

```
poetry run pytest
```

To run linting:

```
poetry run flake8 .
```

To check typing:

```
poetry run mypy .
```

Default installation of virtual environment is in `.venv`. If you need customize parameters you can do it in `setup.cfg`.

All of these steps will be executed in CI pipeline, so we recommend to install `poetry run pre-commit install`, so all checks will run before commiting. You also can customize `.pre-commit-config.yml`


## Submitting your code

1. We use protected `master` branch, so the only way to push code is via Pull-request
2. To implement new issue, you need to create either bugfix/name-of-the-bug or feature/name-of-the-feature
3. One of the commits should say Close #ISSUE_NUMBER, so pull-request will be associated with certain issue
4. Branch should be rebased on top of latest `master` branch
5. You can mark branch as `WIP` until it is finished and all checks are passed


## Other contribution

If you find library useful or want to help us move forward, feel free to star and share the repo to your friends and colleagues. Share with us your experience, best practices and request new features, report bugs.
