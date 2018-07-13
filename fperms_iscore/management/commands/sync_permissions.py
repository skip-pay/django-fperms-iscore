from django.core.management.base import BaseCommand

from is_core.site import get_cores

from fperms import get_perm_model

from ... import enums
from ...mixins import FPermPermission


Perm = get_perm_model()


class Command(BaseCommand):

    def _get_all_core_permissions(self, core):
        f_perm_core_permissions = []
        for permissions in core.permissions.get_permissions():
            for permission in permissions:
                if isinstance(permission, FPermPermission):
                    f_perm_core_permissions.append(permission)
        return f_perm_core_permissions

    def _create_core_permissions(self, core):
        for permission in self._get_all_core_permissions(core):
            Perm.objects.update_or_create(
                type=enums.PERM_TYPE_CORE,
                codename=permission.get_codename(),
                defaults={
                    'name': permission.verbose_name
                }
            )

    def handle(self, *args, **kwargs):
        for core in get_cores():
            self._create_core_permissions(core)
        self.stdout.write('All Core FPerm permissions was updated')
