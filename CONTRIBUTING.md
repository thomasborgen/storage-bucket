# How to contribute

## Dependencies

As a dependency manager we use [poetry](https://github.com/python-poetry/poetry).


To install correct versions of dependencies you would need to do installation via:

```
poetry install
```

## Tests

We use `pytest`, `flake8` and `mypy` as a quality gate. We follow `wemake_python_styleguide` to enforce quality.

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
