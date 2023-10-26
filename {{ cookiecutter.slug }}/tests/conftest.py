# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest  # noqa: F401
{%- if cookiecutter.with_sqlalchemy %}

from {{ cookiecutter.pkg_name }}.database import db  # noqa: F401
{%- endif %}
