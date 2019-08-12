=====
Usage
=====

To use django-fperms-iscore in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'fperms_iscore.apps.FPermsISCoreConfig',
        ...
    )


Cores
-----

You can use `fperms_iscore.permissions.FPermPermission` with your cores to to set dynamic permissions system::


.. code-block:: python

    from is_core.main import UIRESTModelISCore
    from is_core.auth.perm PermissionsSet
    from fperms_iscore.permissions.FPermPermission

    class UserISCore(UIRESTModelISCore):

        model = User
        permissions = PermissionsSet(
            'create': FPermPermission('user__create', 'Create user'),
            'read': FPermPermission('user__read', 'Read user'),
            'update': FPermPermission('user__update', 'Update user'),
            'delete': FPermPermission('user__delete', 'Delete user'),
            'change_password': FPermPermission('user__change_password', register=False),
        )


As you can see class `fperms_iscore.permissions.FPermPermission` has two initial parameters. The first one is code name which is used for permission identification in the database and second one is an optional verbose name for better user experience. The last permission `change_password` has set parameter `register=False`, it means that permission will not be created but it will use already defined permission with same code.

Because this code is little bit complicated there is mixin `fperms_iscore.mixins.PermISCoreMixin` and core class `fperms_iscore.main.PermUIRESTModelISCore` which automatically generates the CRUD permissions::

.. code-block:: python

    from is_core.main import UIRESTModelISCore
    from fperms_iscore.mixins.PermISCoreMixin
    from fperms_iscore.main.PermUIRESTModelISCore

    class UserISCore(PermISCoreMixin, UIRESTModelISCore):

        model = User

    class IssueISCore(PermUIRESTModelISCore):

        model = Issue

.. DANGER::
   Superuser has always access to all operations. His access rights will not depend on the selected permissions or groups.

Commands
--------

We right now have implemented cores with a dynamic permission check. But database permissions should be somehow stored inside a database. The command `sync_permissions` is there for this purpose. The command will create new permissions and update already generated permissions.
