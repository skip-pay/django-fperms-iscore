=============================
django-fperms-iscore
=============================

.. image:: https://badge.fury.io/py/fperms-iscore.svg
    :target: https://badge.fury.io/py/fperms-iscore

.. image:: https://travis-ci.org/Formulka/django-fperms-iscore.svg?branch=master
    :target: https://travis-ci.org/Formulka/django-fperms-iscore

.. image:: https://codecov.io/gh/Formulka/django-fperms-iscore/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Formulka/django-fperms-iscore

Perms for iscore library

Documentation
-------------

The full documentation is at https://django-perms-iscore.readthedocs.io.

Quickstart
----------

Install django-fperms-iscore::

    pip install fperms-iscore

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'fperms_iscore.apps.FPermsIscoreConfig',
        ...
    )

Add django-fperms-iscore's URL patterns:

.. code-block:: python

    from fperms_iscore import urls as fperms_iscore_urls


    urlpatterns = [
        ...
        url(r'^', include(fperms_iscore_urls)),
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
