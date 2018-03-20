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

    # set the extended model for FPerms
    PERM_MODEL = 'fperms_iscore.IsCorePerm'
