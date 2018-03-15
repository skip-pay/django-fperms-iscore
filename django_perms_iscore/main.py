from is_core.main import UIRESTModelISCore


from django_perms_iscore.mixins import PermMixin


class PermUIRESTModelISCore(PermMixin, UIRESTModelISCore):

    abstract = True

