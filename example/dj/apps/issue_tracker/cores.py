from django.contrib.auth.models import User

from issue_tracker.models import Issue
from issue_tracker.forms import UserForm

from fperms.models import Group

from fperms_iscore.forms import GroupForm
from fperms_iscore.main import PermDjangoUiRestCore


class UserCore(PermDjangoUiRestCore):

    model = User
    form_class = UserForm
    fields = ('username', 'first_name', 'last_name', 'is_superuser')
    list_fields = ('id', 'first_name', 'last_name', 'is_superuser')
    form_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'fperms')


class IssueCore(PermDjangoUiRestCore):

    model = Issue
    fields = ('name', 'watched_by', 'created_by', 'solver', 'leader')
    list_fields = ('id', '_obj_name', 'watched_by_string', 'leader__email', 'leader__last_name')


class UserGroupCore(PermDjangoUiRestCore):

    model = Group
    can_create = True

    form_class = GroupForm
    fields = ('codename', 'name', 'fperms', 'fgroups', 'users')
    list_fields = ('id', 'name')
