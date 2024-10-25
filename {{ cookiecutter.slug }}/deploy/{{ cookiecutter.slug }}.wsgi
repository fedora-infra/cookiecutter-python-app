# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from {{ cookiecutter.pkg_name }}.app import create_app


application = create_app()
