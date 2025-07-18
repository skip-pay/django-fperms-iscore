from django.utils.translation import gettext_lazy as _

from .permissions import FPermPermission


class PermCoreMixin:
    """
    Mixin that adds automatic CRUD permission generation to Core classes.

    Generates permissions with pattern: {menu_group}__{operation}
    Operations: create, read, update, delete
    """

    default_permission_classes = ()

    default_permission_verbose_names = {
        'read': _('Can read objects "{model_verbose_name}"'),
        'update': _('Can update objects "{model_verbose_name}"'),
        'delete': _('Can delete objects "{model_verbose_name}"'),
        'create': _('Can create objects "{model_verbose_name}"'),
    }

    def _get_permission_verbose_name(self, permission_name):
        """
        Get verbose name of the permission which can be defined inside property `default_permission_verbose_names`
        :param permission_name: name of the permission
        :return: verbose name of the permission that will be stored in database with `sync_permissions` command
        """
        verbose_name = self.default_permission_verbose_names.get(permission_name)
        return verbose_name.format(
            model_verbose_name_plural=self.get_verbose_name_plural(),
            model_verbose_name=self.get_verbose_name()
        ) if verbose_name else verbose_name

    def _get_default_permission(self, name):
        """
        Method automatically prepares fperms permissions for CRUD.
        """
        return FPermPermission('{}__{}'.format(self.menu_group, name), self._get_permission_verbose_name(name))
