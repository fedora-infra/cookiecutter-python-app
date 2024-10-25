# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from bs4 import BeautifulSoup

from {{ cookiecutter.pkg_name }}.database import db
from {{ cookiecutter.pkg_name }}.models import User


def test_root(client):
    """Test the root page"""
    response = client.get("/")
    assert response.status_code == 200
    page = BeautifulSoup(response.data, "html.parser")
    assert page.title
    assert page.title.string is not None
    assert "{{ cookiecutter.name }}" in page.title.string


def test_profile(client):
    """Test the profile page"""
    user = User(name="testuser", full_name="Test User", timezone="Europe/Paris")
    db.session.add(user)
    db.session.flush()
    response = client.get(f"/user/{user.id}")
    assert response.status_code == 200
    page = BeautifulSoup(response.data, "html.parser")
    assert page.title
    assert page.title.string is not None
    assert "{{ cookiecutter.name }}" in page.title.string
    content = page.select_one("#profile")
    assert content is not None
    assert "Full Name: Test User" in list(content.stripped_strings)
    assert "Timezone: Europe/Paris" in list(content.stripped_strings)
