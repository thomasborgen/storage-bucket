We use `pytest`, `flake8` and `mypy` as a quality gate. We follow [`wemake_python_styleguide`](https://wemake-python-stylegui.de/en/latest/) to enforce quality.

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

All of these steps will be executed in CI pipeline, so we recommend to install `poetry run pre-commit install`, so all checks will run before commiting. You also can customize `.pre-commit-config.yml`
