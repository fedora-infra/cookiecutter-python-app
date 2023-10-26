#!/bin/sh

set -e
set -x

{% if not cookiecutter.with_sqlalchemy %}
rm -rf "{{ cookiecutter.pkg_name }}/database.py"
rm -rf "{{ cookiecutter.pkg_name }}/migrations"
rm -rf "{{ cookiecutter.pkg_name }}/models"
{% endif %}
{% if not cookiecutter.with_cli %}
rm -rf "{{ cookiecutter.pkg_name }}/cli.py"
{% endif %}
{% if not cookiecutter.with_i18n %}
rm -f "babel.cfg"
rm -rf "{{ cookiecutter.pkg_name }}/translations"
{% endif %}

git init .
git ci --allow-empty -s -m "Initial empty commit"
git add .
git ci -s -m "Project creation from the cookiecutter template"
pre-commit install
