from django.db.models import Q
from is_core.auth.main import PermissionsMixin

from django_perms import get_perm_model

from django_perms_iscore import enums
from django_perms_iscore.utils import get_iscore_class_str


Perm = get_perm_model()


class PermIsCoreMixin(PermissionsMixin):

    @classmethod
    def _get_perm(cls, codename, obj):
        perms = Perm.objects.filter(
            Q(
                type=enums.PERM_TYPE_CORE,
                codename=codename,
                core=get_iscore_class_str(cls),
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

    def has_read_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('read', obj=obj))

    def has_create_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('create', obj=obj))

    def has_update_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('update', obj=obj))

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('delete', obj=obj))
