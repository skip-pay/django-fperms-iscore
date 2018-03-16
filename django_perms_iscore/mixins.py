from is_core.auth.main import PermissionsMixin

from django_perms import get_perm_model

from django_perms_iscore import enums
from django_perms_iscore.utils import get_iscore_class_str


class PermIsCoreMixin(PermissionsMixin):

    perm_type = enums.PERM_TYPE_CORE

    @classmethod
    def _get_perm(cls, codename, obj):
        return get_perm_model().objects.get(
            type=cls.perm_type,
            codename=codename,
            core=get_iscore_class_str(cls),
            object_id=obj.pk if obj else None,
        )

    def has_read_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('read', obj=obj))

    def has_create_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('create', obj=obj))

    def has_update_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('update', obj=obj))

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.perms.has_perm(self._get_perm('delete', obj=obj))
