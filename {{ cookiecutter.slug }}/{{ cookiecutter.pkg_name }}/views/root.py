# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from flask import render_template

from {{ cookiecutter.pkg_name }}.database import db, get_or_404
from {{ cookiecutter.pkg_name }}.models import User

from . import blueprint as bp


@bp.route("/")
def root():
    users = db.session.query(User).all()
    return render_template("index.html", users=users)


@bp.route("/user/<int:user_id>")
def profile(user_id):
    user = get_or_404(User, user_id)
    return render_template("profile.html", user=user)
