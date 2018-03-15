from django.utils.translation import ugettext_lazy as _

from django_perms.enums import *

PERM_TYPE_CORE = 'core'

IS_CORE_PERM_TYPE_CHOICES = (
    (PERM_TYPE_CORE, _('core')),
)

PERM_TYPE_CHOICES = settings.PERM_TYPE_CHOICES + IS_CORE_PERM_TYPE_CHOICES
