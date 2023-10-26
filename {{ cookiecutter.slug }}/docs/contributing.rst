============
Contributing
============

Thanks for considering contributing to {{ cookiecutter.name }}, we really appreciate it!

Quickstart:

1. Look for an `existing issue <{{ cookiecutter.github_url }}/issues>`_ about the bug or
   feature you're interested in. If you can't find an existing issue, create a
   `new one <{{ cookiecutter.github_url }}/issues/new>`_.

2. Fork the `repository on GitHub <{{ cookiecutter.github_url }}>`_.

3. Fix the bug or add the feature, and then write one or more tests which show
   the bug is fixed or the feature works.

4. Submit a pull request and wait for a maintainer to review it.

More detailed guidelines to help ensure your submission goes smoothly are
below.

.. note:: If you do not wish to use GitHub, please send patches to
          infrastructure@lists.fedoraproject.org.

Development Environment
=======================
Vagrant allows contributors to get quickly up and running with a {{ cookiecutter.name }}
development environment by automatically configuring a virtual machine. To get started,
first install the Vagrant and Virtualization packages needed, and start the libvirt service::

    $ sudo dnf install ansible libvirt vagrant-libvirt vagrant-sshfs vagrant-hostmanager
    $ sudo systemctl enable libvirtd
    $ sudo systemctl start libvirtd

Check out the code and run ``vagrant up``::

    $ git clone {{ cookiecutter.github_url }}
    $ cd {{ cookiecutter.slug }}
    $ vagrant up

Next, SSH into your newly provisioned development environment:

    $ vagrant ssh

Note that the ``/home/vagrant/{{ cookiecutter.slug }}`` folder contains the source of the
git checkout on your host. Any changes to the files in that directory on the host will be
automatically synced to the VM.


Guidelines
==========

Python Support
--------------
{{ cookiecutter.name }} supports Python 3.6 or greater. This is automatically enforced by the
continuous integration (CI) suite.


Code Style
----------
We follow the `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide
for Python. This is automatically enforced by the CI suite.

We are using `Black <https://github.com/psf/black>` to automatically format
the source code. It is also checked in CI. The Black webpage contains
instructions to configure your editor to run it on the files you edit.

Handle every possible case, and do so where it makes sense.


Security
--------
Remember to keep the code simple enough that it can be easily reviewed for
security concerns.

Code that touches security-critical paths must be signed off by **two** people.
People who sign off are agreeing to have reviewed the code thoroughly and
thought about edge cases.


Tests
-----
The test suites can be run using `tox <http://tox.readthedocs.io/>`_ by simply
running ``tox`` from the repository root. All code must have test coverage or
be explicitly marked as not covered using the ``#  pragma: no cover`` comment.
This should only be done if there is a good reason to not write tests.

Your pull request should contain tests for your new feature or bug fix. If
you're not certain how to write tests, we will be happy to help you.


Release Notes
-------------

To add entries to the release notes, create a file in the ``news`` directory in the
``source.type`` name format, where the ``source`` part of the filename is:

* ``42`` when the change is described in issue ``42``
* ``PR42`` when the change has been implemented in pull request ``42``, and
  there is no associated issue
* ``Cabcdef`` when the change has been implemented in changeset ``abcdef``, and
  there is no associated issue or pull request.

And where the extension ``type`` is one of:

* ``security``: for security fixes
* ``removed``: for removed features (this will be a backwards incompatible change)
* ``deprecated``: for deprecated features
* ``added``: for new features
* ``fixed``: for bug fixes
* ``changed``: for other changes

The content of the file will end up in the release notes. It should not end
with a ``.`` (full stop).

A preview of the release notes can be generated with ``towncrier build --draft``.


Licensing
---------

Your commit messages must include a Signed-off-by tag with your name and e-mail
address, indicating that you agree to the `Developer Certificate of Origin
<https://developercertificate.org/>`_ version 1.1::

	Developer Certificate of Origin
	Version 1.1

	Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
	1 Letterman Drive
	Suite D4700
	San Francisco, CA, 94129

	Everyone is permitted to copy and distribute verbatim copies of this
	license document, but changing it is not allowed.


	Developer's Certificate of Origin 1.1

	By making a contribution to this project, I certify that:

	(a) The contribution was created in whole or in part by me and I
	    have the right to submit it under the open source license
	    indicated in the file; or

	(b) The contribution is based upon previous work that, to the best
	    of my knowledge, is covered under an appropriate open source
	    license and I have the right under that license to submit that
	    work with modifications, whether created in whole or in part
	    by me, under the same open source license (unless I am
	    permitted to submit under a different license), as indicated
	    in the file; or

	(c) The contribution was provided directly to me by some other
	    person who certified (a), (b) or (c) and I have not modified
	    it.

	(d) I understand and agree that this project and the contribution
	    are public and that a record of the contribution (including all
	    personal information I submit with it, including my sign-off) is
	    maintained indefinitely and may be redistributed consistent with
	    this project or the open source license(s) involved.

Use ``git commit -s`` to add the Signed-off-by tag.


Releasing
---------

When cutting a new release, follow these steps:

#. Update the version in ``pyproject.toml`` or by running ``poetry version [major|minor|patch]``
#. Generate the release notes by running ``towncrier build``
{% if cookiecutter.with_i18n %}
#. Compile the translations with
   ``poetry run pybabel compile -d {{ cookiecutter.pkg_name }}/translations``
{% endif %}
#. Commit the changes
#. Tag the commit with ``-s`` to generate a signed tag
#. Push those changes to the upstream Github repository (via a PR or not)
#. Push the tag using ``git push --tags``. The new version will be
   automatically published to PyPI when CI passes, and a release will be
   created in GitHub.
{%- if cookiecutter.with_i18n %}


Translations
------------

To extract the messages.pot that is in {{ cookiecutter.pkg_name }}/translations/messages.pot,
use::

  poetry run pybabel extract -F babel.cfg -o {{ cookiecutter.pkg_name }}/translations/messages.pot {{ cookiecutter.pkg_name }}

This will update the messages.pot with the newest strings that have been flagged in the
templates and code.

To add a new language, use the command::

  poetry run pybabel init -i {{ cookiecutter.pkg_name }}/translations/messages.pot -d {{ cookiecutter.pkg_name }}/translations/ -l fr_FR

To update all created languages with the newest strings in messages.pot, use::

  poetry run pybabel update -i {{ cookiecutter.pkg_name }}/translations/messages.pot -d {{ cookiecutter.pkg_name }}/translations

To compile the translations in updated .mo files into what {{ cookiecutter.name }} can use,
use the command::

  poetry run pybabel compile -d {{ cookiecutter.pkg_name }}/translations
{%- endif %}
