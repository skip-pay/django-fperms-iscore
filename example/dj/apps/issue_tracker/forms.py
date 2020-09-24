from django.utils.translation import ugettext_lazy as _

from fperms import get_perm_model

from fperms_iscore.forms import PermsFormMixin, GroupsFormMixin

from is_core.forms.models import SmartModelForm, ModelMultipleChoiceField


class UserForm(PermsFormMixin, GroupsFormMixin):
    pass

