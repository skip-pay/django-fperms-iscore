from django.db.models import Q
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from fperms import get_perm_model

from fperms_iscore import enums

from is_core.auth.permissions import BasePermission, IsSuperuser, PermissionsSet


Perm = get_perm_model()


class FPermPermission(BasePermission):

    def __init__(self, group_name, name, verbose_name=None):
        self.group_name = group_name
        self.name = name
        self.verbose_name = verbose_name

    def get_codename(self):
        return '__'.join((self.group_name, self.name))

    def _get_perm(self, codename, obj):
        perms = Perm.objects.filter(
            Q(
                type=enums.PERM_TYPE_CORE,
                codename=codename,
            ),
            Q(
                Q(object_id=obj.pk if obj else None) |
                Q(object_id=None)
            )
        )
        try:
            return perms.get()
        except Perm.DoesNotExist:
            return None

    def has_permission(self, name, request, view, obj=None):
        return request.user.perms.has_perm(self._get_perm(self.get_codename(), obj=obj))


class PermISCoreMixin:

    default_permission_classes = ()

    default_permission_verbose_names = {
        'read': _('Can read {model_verbose_name}'),
        'update': _('Can update {model_verbose_name}'),
        'delete': _('Can delete {model_verbose_name}'),
        'create': _('Can create {model_verbose_name}'),
    }

    def get_permission_verbose_name(self, permission_name):
        verbose_name = self.default_permission_verbose_names.get(permission_name)
        return verbose_name.format(
            model_verbose_name=self.model._meta.verbose_name
        ) if verbose_name else verbose_name

    @cached_property
    def permissions(self):
        return PermissionsSet(
            **{
                k: [p() for p in permission_classes] + [
                    FPermPermission(self.menu_group, k, self.get_permission_verbose_name(k))
                ] for k, permission_classes in self.permissions_classes.items()
            },
            **self.extra_permissions
        )
