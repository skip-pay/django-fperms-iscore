from germanium.decorators import login
from germanium.test_cases.client import ClientTestCase
from germanium.tools.http import assert_http_redirect, assert_http_ok, assert_http_forbidden, assert_http_bad_request, assert_http_accepted

from fperms.models import Perm

from .test_case import HelperTestCase, AsSuperuserTestCase


class UIPermissionsTestCase(AsSuperuserTestCase, HelperTestCase, ClientTestCase):

    def authorize(self, username, password):
        resp = self.post('/login/', {'username': username, 'password': password})
        assert_http_redirect(resp)

    def test_non_logged_user_should_receive_302(self):
        resp = self.get('/user/')
        assert_http_redirect(resp)

    @login(is_superuser=False)
    def test_home_view_should_return_ok_for_all_users(self):
        resp = self.get('/')
        assert_http_ok(resp)

    @login(is_superuser=False)
    def test_home_view_should_return_ok_for_superuser(self):
        resp = self.get('/')
        assert_http_ok(resp)

    @login(is_superuser=True)
    def test_superuser_should_do_all_operations(self):
        issue = self.create_issue()
        user = self.create_user('new_user', 'password', 'test@email.com')

        # List
        assert_http_ok(self.get('/user/'))
        assert_http_ok(self.get('/issue/'))

        # Add
        assert_http_ok(self.get('/user/add/'))
        assert_http_ok(self.get('/issue/add/'))
        assert_http_ok(self.post('/user/add/', {}))
        assert_http_ok(self.post('/issue/add/', {}))

        # Detail
        assert_http_ok(self.get('/user/{}/'.format(user.pk)))
        assert_http_ok(self.get('/issue/{}/'.format(issue.pk)))
        assert_http_ok(self.post('/user/{}/'.format(user.pk), {}))
        assert_http_ok(self.post('/issue/{}/'.format(issue.pk), {}))

    @login(is_superuser=False)
    def test_user_without_permission_should_do_nothing(self):
        issue = self.create_issue()
        user = self.create_user('new_user', 'password', 'test@email.com')

        # List
        assert_http_forbidden(self.get('/user/'))
        assert_http_forbidden(self.get('/issue/'))

        # Add
        assert_http_forbidden(self.get('/user/add/'))
        assert_http_forbidden(self.get('/issue/add/'))
        assert_http_forbidden(self.post('/user/add/', {}))
        assert_http_forbidden(self.post('/issue/add/', {}))

        # Detail
        assert_http_forbidden(self.get('/user/{}/'.format(user.pk)))
        assert_http_forbidden(self.get('/issue/{}/'.format(issue.pk)))
        assert_http_forbidden(self.post('/user/{}/'.format(user.pk), {}))
        assert_http_forbidden(self.post('/issue/{}/'.format(issue.pk), {}))

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

        # List
        assert_http_forbidden(self.get('/user/'))
        assert_http_ok(self.get('/issue/'))

        # Add
        assert_http_forbidden(self.get('/user/add/'))
        assert_http_ok(self.get('/issue/add/'))
        assert_http_forbidden(self.post('/user/add/', {}))
        assert_http_ok(self.post('/issue/add/', {}))

        # Detail
        assert_http_ok(self.get('/user/{}/'.format(user.pk)))
        assert_http_ok(self.get('/issue/{}/'.format(issue.pk)))
        assert_http_ok(self.post('/user/{}/'.format(user.pk), {}))
        assert_http_forbidden(self.post('/issue/{}/'.format(issue.pk), {}))
