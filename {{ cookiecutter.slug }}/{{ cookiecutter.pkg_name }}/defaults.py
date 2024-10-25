# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

# This file contains the default configuration values

TEMPLATES_AUTO_RELOAD = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "sqlite:///../{{ cookiecutter.slug }}.db"

HEALTHZ = {
    "live": "{{ cookiecutter.pkg_name }}.utils.healthz.liveness",
    "ready": "{{ cookiecutter.pkg_name }}.utils.healthz.readiness",
}
