# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from werkzeug.utils import find_modules, import_string


def import_all(import_name):
    for module in find_modules(import_name, include_packages=True, recursive=True):
        import_string(module)
