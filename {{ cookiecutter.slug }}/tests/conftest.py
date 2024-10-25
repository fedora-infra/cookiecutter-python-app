# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

{% if cookiecutter.with_flask -%}
import os
{%- endif %}
import pytest {%- if not cookiecutter.with_flask %}  # noqa: F401 {%- endif %}

{% if cookiecutter.with_sqlalchemy -%}
from {{ cookiecutter.pkg_name }}.database import db {%- if not cookiecutter.with_flask %}  # noqa: F401 {%- endif %}
{%- endif %}
{% if cookiecutter.with_flask -%}
from {{ cookiecutter.pkg_name }}.app import create_app


@pytest.fixture
def app(tmpdir):
    app = create_app()
    app.config.from_object("tests.app_config")
    # Setup the DB
    db_path = os.path.join(tmpdir, "database.sqlite")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    with app.app_context():
        db.manager.create()
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
{%- endif %}
