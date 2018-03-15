=============================
django-perms-iscore
=============================

.. image:: https://badge.fury.io/py/django-perms-iscore.svg
    :target: https://badge.fury.io/py/django-perms-iscore

.. image:: https://travis-ci.org/Formulka/django-perms-iscore.svg?branch=master
    :target: https://travis-ci.org/Formulka/django-perms-iscore

.. image:: https://codecov.io/gh/Formulka/django-perms-iscore/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Formulka/django-perms-iscore

Perms for iscore library 

Documentation
-------------

The full documentation is at https://django-perms-iscore.readthedocs.io.

Quickstart
----------

Install django-perms-iscore::

    pip install django-perms-iscore

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_perms_iscore.apps.DjangoPermsIscoreConfig',
        ...
    )

Add django-perms-iscore's URL patterns:

.. code-block:: python

    from django_perms_iscore import urls as django_perms_iscore_urls


    urlpatterns = [
        ...
        url(r'^', include(django_perms_iscore_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
