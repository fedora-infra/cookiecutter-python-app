# CookieCutter for Fedora Infrastructure Python apps

This is a [CookieCutter](https://cookiecutter.readthedocs.io) template directory for
Fedora Infrastructure Python apps.

Use it with:
```
cookiecutter gh:fedora-infra/cookiecutter-python-app
```

It will ask you for the application name and some other variables, and will create the package
structure for you.


## Features

Here are the libraries and services that are integrated:

- Dependency management with [Poetry](https://python-poetry.org/)
- OpenShift support with [S2I](https://github.com/sclorg/s2i-python-container)
- Formatting with [Black](https://github.com/psf/black)
- Various checks like [ruff](https://beta.ruff.rs),
  [liccheck](https://github.com/dhatim/python-license-check),
  [rstcheck](https://github.com/myint/rstcheck), and
  [reuse](https://reuse.software/)
- Unit tests with [Pytest](https://pytest.org/), [Coverage](https://coverage.readthedocs.io)
  & [Tox](tox.readthedocs.io/)
- Documentation with [Sphinx](https://www.sphinx-doc.org/)
- Changelog generation with [Towncrier](https://towncrier.readthedocs.io/)
- CI with Github Actions
- [Renovate](https://github.com/apps/renovate)
- [Pre-Commit](https://pre-commit.com/)
- Publication to PyPI with [PyPI Trusted Publishing](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
- Creation of Github Releases with Github Actions
- Optionaly, CLI with [Click](click.palletsprojects.com/)
- Optionaly, database support with [SQLAlchemy](https://www.sqlalchemy.org/)
  & [Alembic](https://alembic.sqlalchemy.org)
- Optionaly, Flask security with [Flask-Talisman](https://pypi.org/project/flask-talisman/)


## Requirements

You need to have these tools installed:
- [CookieCutter](https://cookiecutter.readthedocs.io/) >= 2.2.0
- Git
- [Poetry](https://python-poetry.org/) >= 1.2
- [Pre-Commit](https://pre-commit.com/)


## Testing

There are some checks to make sure the templated app pass its own unit tests.
You can run those checks with:

```
pytest -s tests
```
