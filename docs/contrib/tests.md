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
