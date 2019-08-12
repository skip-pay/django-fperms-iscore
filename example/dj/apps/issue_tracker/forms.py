from django.utils.translation import ugettext_lazy as _

from fperms import get_perm_model

from is_core.forms.models import SmartModelForm, ModelMultipleChoiceField


class PermissionsForm(SmartModelForm):

    perms = ModelMultipleChoiceField(
        label=_('Permissions'), queryset=get_perm_model().objects.all(), required=False
    )

    def _init_perms(self, field):
        if self.instance.pk:
            field.initial = self.instance.perms.values_list('pk', flat=True)

    def _post_save(self, obj):
        obj.perms.set(self.cleaned_data['perms'])
