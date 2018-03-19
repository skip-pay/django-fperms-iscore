from django.contrib.auth.models import User

from issue_tracker.models import Issue
from issue_tracker.forms import UserForm

from django_perms_iscore.main import PermUIRESTModelISCore

from .resources import NumberOfUserIssuesResource


class UserIsCore(PermUIRESTModelISCore):
    model = User
    form_class = UserForm
    list_display = ('id', '_obj_name')

    def has_read_permission(self, request, obj=None):
        return super().has_read_permission(request, obj) or (obj and obj.pk == request.user.pk)

    def has_update_permission(self, request, obj=None):
        return super().has_update_permission(request, obj) or (
            (obj and obj.pk == request.user.pk) or request.user.is_superuser
        )

    def get_queryset(self, request):
        qs = super(UserIsCore, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(pk=request.user.pk)
        return qs

    def get_rest_patterns(self):
        rest_patterns = super(UserIsCore, self).get_rest_patterns()
        rest_patterns['api-user-issue'] = self.default_rest_pattern_class(
            'api-number-issues', self.site_name, r'(?P<pk>[-\w]+)/issue-number/', NumberOfUserIssuesResource, self)
        return rest_patterns


class IssueIsCore(PermUIRESTModelISCore):
    model = Issue
    list_display = ('id', '_obj_name', 'watched_by_string', 'leader__email', 'leader__last_name')

    def has_rest_create_permission(self, request, obj=None, via=None):
        return bool(via) and via[0].model == User
