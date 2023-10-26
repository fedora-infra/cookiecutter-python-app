# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

import click
{% if cookiecutter.with_sqlalchemy -%}
from sqlalchemy_helpers import SyncResult

from {{ cookiecutter.pkg_name }}.database import db as db_manager
{% endif %}

@click.group()
def main():
    pass
{%- if cookiecutter.with_sqlalchemy %}


@main.group()
def db():
    """Work with the database."""
    pass


@db.command()
def sync():
    """Set up the configured database."""
    result = db_manager.sync()
    if result == SyncResult.CREATED:
        click.echo("Database created.")
    elif result == SyncResult.UPGRADED:
        click.echo("Database upgraded.")
    elif result == SyncResult.ALREADY_UP_TO_DATE:
        click.echo("Database already up-to-date.")
    else:
        click.echo(f"Unexpected sync result: {result}", err=True)
{%- endif %}
