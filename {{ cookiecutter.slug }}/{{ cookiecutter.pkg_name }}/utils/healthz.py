# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from flask_healthz import HealthError
from sqlalchemy_helpers.manager import DatabaseStatus

from {{ cookiecutter.pkg_name }}.database import db


def liveness():
    pass


def readiness():
    try:
        status = db.manager.get_status()
    except Exception as e:
        raise HealthError(f"Can't get the database status: {e}") from e
    if status is DatabaseStatus.NO_INFO:
        raise HealthError("Can't connect to the database")
    if status is DatabaseStatus.UPGRADE_AVAILABLE:
        raise HealthError("The database schema needs to be updated")
