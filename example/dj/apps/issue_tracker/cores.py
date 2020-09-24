from django.contrib.auth.models import User

from issue_tracker.models import Issue
from issue_tracker.forms import UserForm

from fperms.models import Group

from fperms_iscore.forms import GroupForm
from fperms_iscore.main import PermUIRESTModelISCore


class UserISCore(PermUIRESTModelISCore):

    model = User
    form_class = UserForm
    ui_list_fields = ('id', 'first_name', 'last_name', 'is_superuser')
    form_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'fperms')


class IssueISCore(PermUIRESTModelISCore):

    model = Issue
    ui_list_fields = ('id', '_obj_name', 'watched_by_string', 'leader__email', 'leader__last_name')


class UserGroupISCore(PermUIRESTModelISCore):

    model = Group
    can_create = True

    form_class = GroupForm
    form_fields = (
        'id', 'name', 'fperms', 'fgroups'
    )
    ui_list_fields = ('id', 'name')
