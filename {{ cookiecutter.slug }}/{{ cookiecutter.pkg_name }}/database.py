# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Use sqlalchemy-helpers.

Import the functions we will use in the main code and in migrations.
"""

from sqlalchemy_helpers import (  # noqa: F401
    Base,
    DatabaseManager,
    exists_in_db,
    get_or_create,
    is_sqlite,
)

from {{ cookiecutter.pkg_name }}.config import get_config


db_config = get_config().database.model_dump()
db = DatabaseManager(
    str(db_config["sqlalchemy"]["url"]),
    str(db_config["alembic"]["migrations_path"]),
    engine_args=db_config["sqlalchemy"],
)
