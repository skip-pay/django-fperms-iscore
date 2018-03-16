from is_core.main import UIRESTModelISCore


from django_perms_iscore.mixins import PermIsCoreMixin


class PermUIRESTModelISCore(PermIsCoreMixin, UIRESTModelISCore):

    abstract = True

