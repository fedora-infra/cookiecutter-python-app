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
rm -f "{{ cookiecutter.pkg_name }}/l10n.py"
{% endif %}
{% if not cookiecutter.with_flask %}
rm -rf "deploy"
rm -f "{{ cookiecutter.slug }}.cfg.default"
rm -f "{{ cookiecutter.pkg_name }}/app.py"
rm -f "{{ cookiecutter.pkg_name }}/defaults.py"
rm -f "{{ cookiecutter.pkg_name }}/l10n.py"
rm -rf "{{ cookiecutter.pkg_name }}/templates/"
rm -rf "{{ cookiecutter.pkg_name }}/utils/"
rm -rf "{{ cookiecutter.pkg_name }}/views/"
rm -rf "{{ cookiecutter.pkg_name }}/static/"
rm -f "tests/app_config.py"
rm -f "tests/test_healthz.py"
rm -f "tests/test_root.py"
{% endif %}

black .
ruff check --fix .
git init .
git commit --allow-empty -s -m "Initial empty commit"
git add .
git commit -s -m "Project creation from the cookiecutter template"
pre-commit install
