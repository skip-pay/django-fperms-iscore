from django.contrib.auth.models import User, Group

from issue_tracker.models import Issue
from issue_tracker.forms import PermissionsForm

from fperms_iscore.main import PermUIRESTModelISCore


class UserISCore(PermUIRESTModelISCore):

    model = User
    form_class = PermissionsForm
    ui_list_fields = ('id', 'first_name', 'last_name', 'is_superuser')
    form_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'groups', 'perms')


class IssueISCore(PermUIRESTModelISCore):

    model = Issue
    ui_list_fields = ('id', '_obj_name', 'watched_by_string', 'leader__email', 'leader__last_name')


class UserGroupISCore(PermUIRESTModelISCore):

    model = Group
    can_create = True

    form_class = PermissionsForm
    form_fields = (
        'id', 'name', 'perms'
    )
    ui_list_fields = ('id', 'name', 'perms')
