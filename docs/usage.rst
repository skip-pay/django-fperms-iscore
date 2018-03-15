=====
Usage
=====

To use django-perms-iscore in a project, add it to your `INSTALLED_APPS`:

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
