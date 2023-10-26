# SPDX-FileCopyrightText: Contributors to the Fedora Project
#
# SPDX-License-Identifier: GPL-3.0-or-later

from sqlalchemy import Column, Integer, Unicode

from {{ cookiecutter.pkg_name }}.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    name = Column(Unicode(254), index=True, unique=True, nullable=False)
    full_name = Column(Unicode(254), nullable=False)
    timezone = Column(Unicode(127), nullable=True)
