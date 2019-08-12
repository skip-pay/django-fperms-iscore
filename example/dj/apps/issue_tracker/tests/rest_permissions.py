from germanium.decorators import login
from germanium.test_cases.rest import RESTTestCase
from germanium.tools.http import assert_http_redirect, assert_http_ok, assert_http_forbidden, assert_http_bad_request, assert_http_accepted

from fperms.models import Perm

from .test_case import HelperTestCase, AsSuperuserTestCase


class RESTPermissionsTestCase(AsSuperuserTestCase, HelperTestCase, RESTTestCase):

    def authorize(self, username, password):
        resp = self.c.post('/login/', {'username': username, 'password': password})
        assert_http_redirect(resp)

    @login(is_superuser=True)
    def test_superuser_should_do_all_operations(self):
        issue = self.create_issue()
        user = self.create_user('new_user', 'password', 'test@email.com')

        # Generic read, post
        assert_http_ok(self.get('/api/user/'))
        assert_http_ok(self.get('/api/issue/'))
        assert_http_bad_request(self.post('/api/user/', {}))
        assert_http_bad_request(self.post('/api/issue/', {}))

        # API
        # Generic read, put, patch, delete
        assert_http_ok(self.get('/api/user/{}/'.format(user.pk)))
        assert_http_ok(self.get('/api/issue/{}/'.format(issue.pk)))
        assert_http_bad_request(self.put('/api/user/{}/'.format(user.pk), {}))
        assert_http_bad_request(self.put('/api/issue/{}/'.format(issue.pk), {}))
        assert_http_accepted(self.delete('/api/user/{}/'.format(user.pk)))
        assert_http_accepted(self.delete('/api/issue/{}/'.format(issue.pk)))

    @login(is_superuser=False)
    def test_user_without_permission_should_do_nothing(self):
        issue = self.create_issue()
        user = self.create_user('new_user', 'password', 'test@email.com')

        # API
        # Generic read, post
        assert_http_forbidden(self.get('/api/user/'))
        assert_http_forbidden(self.get('/api/issue/'))
        assert_http_forbidden(self.post('/api/user/', {}))
        assert_http_forbidden(self.post('/api/issue/', {}))

        # API
        # Generic read, put, patch, delete
        assert_http_forbidden(self.get('/api/user/{}/'.format(user.pk)))
        assert_http_forbidden(self.get('/api/issue/{}/'.format(issue.pk)))
        assert_http_forbidden(self.put('/api/user/{}/'.format(user.pk), {}))
        assert_http_forbidden(self.put('/api/issue/{}/'.format(issue.pk), {}))
        assert_http_forbidden(self.delete('/api/user/{}/'.format(user.pk)))
        assert_http_forbidden(self.delete('/api/issue/{}/'.format(issue.pk)))

    @login(is_superuser=False)
    def test_user_with_permission_should_do_allowed_operations(self):
        self.sync_permissions()
        issue = self.create_issue()
        user = self.create_user('new_user', 'password', 'test@email.com')

        logged_user = self.logged_user.user

        issue_read_permission = Perm.objects.get(codename='{}__{}'.format('issue', 'read'))
        issue_create_permission = Perm.objects.get(codename='{}__{}'.format('issue', 'create'))
        user_delete_permission = Perm.objects.get(codename='{}__{}'.format('user', 'delete'))
        user_update_permission = Perm.objects.get(codename='{}__{}'.format('user', 'update'))

        logged_user.perms.add(
            issue_read_permission, issue_create_permission, user_delete_permission, user_update_permission
        )

        # API
        # Generic read, post
        assert_http_forbidden(self.get('/api/user/'))
        assert_http_ok(self.get('/api/issue/'))
        assert_http_forbidden(self.post('/api/user/', {}))
        assert_http_bad_request(self.post('/api/issue/', {}))

        # API
        # Generic read, put, patch, delete
        assert_http_forbidden(self.get('/api/user/{}/'.format(user.pk)))
        assert_http_ok(self.get('/api/issue/{}/'.format(issue.pk)))
        assert_http_bad_request(self.put('/api/user/{}/'.format(user.pk), {}))
        assert_http_forbidden(self.put('/api/issue/{}/'.format(issue.pk), {}))
        assert_http_accepted(self.delete('/api/user/{}/'.format(user.pk)))
        assert_http_forbidden(self.delete('/api/issue/{}/'.format(issue.pk)))
