=====
Usage
=====

To use django-fperms-iscore in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'fperms_iscore.apps.FPermsIscoreConfig',
        ...
    )

Add fperms-iscore's URL patterns:

.. code-block:: python

    from fperms_iscore import urls as fperms_iscore_urls


    urlpatterns = [
        ...
        url(r'^', include(fperms_iscore_urls)),
        ...
    ]
