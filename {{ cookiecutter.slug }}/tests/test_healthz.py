# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import current_app
from sqlalchemy_helpers.manager import DatabaseStatus

from {{ cookiecutter.pkg_name }}.database import db


def test_healthz_liveness(client):
    """Test the /healthz/live check endpoint"""
    response = client.get("/healthz/live")
    assert response.status_code == 200
    assert response.json == {"status": 200, "title": "OK"}


def test_healthz_readiness_ok(client):
    """Test the /healthz/ready check endpoint"""
    response = client.get("/healthz/ready")
    print(response.data)
    assert response.status_code == 200
    assert response.json == {"status": 200, "title": "OK"}


def test_healthz_readiness_unavailable(client, mocker, tmpdir):
    """Test the /healthz/ready check endpoint when the DB is not ready"""
    db.manager.drop()
    mocker.patch.dict(
        current_app.config, {"SQLALCHEMY_DATABASE_URI": f"sqlite:///{tmpdir}/new.db"}
    )
    response = client.get("/healthz/ready")
    assert response.status_code == 503
    assert response.json == {"status": 503, "title": "Can't connect to the database"}


def test_healthz_readiness_needs_upgrade(client, mocker):
    """Test the /healthz/ready check endpoint when the DB schema is old"""
    mocker.patch.object(
        db.manager, "get_status", return_value=DatabaseStatus.UPGRADE_AVAILABLE
    )
    response = client.get("/healthz/ready")
    assert response.status_code == 503
    assert response.json == {
        "status": 503,
        "title": "The database schema needs to be updated",
    }


def test_healthz_readiness_exception(client, mocker):
    """Test the /healthz/ready check endpoint when the DB is wrong"""
    mocker.patch.dict(
        current_app.config, {"SQLALCHEMY_DATABASE_URI": "sqlite:////does/not/exist"}
    )
    response = client.get("/healthz/ready")
    assert response.status_code == 503
    assert response.json["status"] == 503
    assert response.json["title"].startswith(
        "Can't get the database status: (sqlite3.OperationalError) "
        "unable to open database file"
    )
