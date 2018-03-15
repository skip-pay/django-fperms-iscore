# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_perms.models import BasePerm

from django_perms_iscore import enums


class IsCorePerm(BasePerm):

    PERM_TYPE_CHOICES = enums.PERM_TYPE_CHOICES

    core = models.CharField(
        _('core'),
        max_length=100,
    )

    class Meta:
        unique_together = (
            ('type', 'codename', 'content_type', 'object_id', 'field_name', 'core'),
        )

    @property
    def _core_perm_name(self):
        return _('core %s') % (
            self.core,
        )

    @property
    def _core_perm_str_args(self):
        return [
            self.type,
            self.core,
            self.codename,
        ]

    @classmethod
    def get_perm_kwargs(cls, perm, obj=None):
        perm_type, perm_arg_string = perm.split('.', 1)

        if perm_type == enums.PERM_TYPE_CORE:
            core, codename = perm_arg_string.rsplit('.', 1)

            return dict(
                type=perm_type,
                codename=codename,
                core=core
            )

        return super().get_perm_kwargs(perm=perm, obj=obj)
