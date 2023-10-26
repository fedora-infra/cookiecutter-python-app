import os
from subprocess import run, PIPE

import pytest
from cookiecutter.main import cookiecutter


class Templated:
    def __init__(self, dest_dir):
        assert os.path.exists(dest_dir)
        self.dest_dir = dest_dir
        self.name = os.path.basename(self.dest_dir)
        self.pkgname = self.name.replace("-", "_")

    @classmethod
    def create(cls, tmpdir, **kwargs):
        context = {
            "name": "Unit Testing Project",
        }
        context.update(kwargs)
        dest_dir = cookiecutter(
            ".",
            no_input=True,
            output_dir=tmpdir,
            default_config=True,
            extra_context=context,
        )
        return cls(dest_dir)

    def run(self, *args, **kwargs):
        env = os.environ.copy()
        env.update(
            {
                "PRE_COMMIT_HOME": os.path.normpath(
                    os.path.join(self.dest_dir, "..", "pre-commit")
                ),
                "POETRY_CACHE_DIR": os.path.normpath(
                    os.path.join(self.dest_dir, "..", "poetry")
                ),
            }
        )
        return run(*args, **kwargs, cwd=self.dest_dir, check=True, env=env, text=True)


@pytest.mark.parametrize("with_sqlalchemy", [False, True])
@pytest.mark.parametrize("with_cli", [False, True])
@pytest.mark.parametrize("with_i18n", [False, True])
def test_basic_creation(tmpdir, with_sqlalchemy, with_cli, with_i18n):
    templated = Templated.create(
        tmpdir=tmpdir,
        with_sqlalchemy=with_sqlalchemy,
        with_cli=with_cli,
        with_i18n=with_i18n,
    )
    # We can't have 100% coverage with a templated project
    templated.run(["sed", "-i", "-e", "/^fail_under = 100/d", "pyproject.toml"])
    # Make sure the unit tests work
    templated.run(["tox", "-e", "checks,licenses,docs"])


def test_alembic_command(tmpdir):
    templated = Templated.create(tmpdir=tmpdir, with_sqlalchemy=True, with_cli=True)
    templated.run(["poetry", "install"])
    # Latest available revision
    result = templated.run(
        [
            "poetry",
            "run",
            "alembic",
            "-c",
            "unit_testing_project/migrations/alembic.ini",
            "heads",
        ],
        stdout=PIPE,
    )
    assert result.stdout.strip() == "initial (head)"
    # Current DB revision when the DB has not been created yet
    result = templated.run(
        [
            "poetry",
            "run",
            "alembic",
            "-c",
            "unit_testing_project/migrations/alembic.ini",
            "current",
        ],
        stdout=PIPE,
    )
    assert result.stdout == ""
    # Create the DB
    result = templated.run(
        ["poetry", "run", "unit-testing-project", "db", "sync"], stdout=PIPE
    )
    assert result.stdout.strip() == "Database created."
    # Current DB revision when the DB has been created
    result = templated.run(
        [
            "poetry",
            "run",
            "alembic",
            "-c",
            "unit_testing_project/migrations/alembic.ini",
            "current",
        ],
        stdout=PIPE,
    )
    assert result.stdout.strip() == "initial (head)"
