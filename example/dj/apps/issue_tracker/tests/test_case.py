from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command

from germanium.test_cases.auth import UserProxy

from .factories import UserFactory, IssueFactory


class HelperTestCase(object):

    user_index = 1
    issue_index = 1

    def get_pk(self, resp):
        return self.deserialize(resp).get('id')

    def get_user_data(self, prefix=''):
        result = {
            'username': '%suser_%s' % (prefix, self.user_index),
            'email': '%suser_%s@test.cz' % (prefix, self.user_index),
            'password': 'super secret password'
        }
        self.user_index += 1
        return result

    def get_issue_data(self, prefix='', exclude=None):
        exclude = exclude or []
        result = {
            'name': 'Issue %s' % self.issue_index,
            'created_by': self.get_user_data(prefix),
            'leader': self.get_user_data(prefix)
        }
        self.issue_index += 1
        for field in exclude:
            del result[field]
        return result

    def create_user(self, username, email, password, **kwargs):
        return UserFactory(username=username, email=email, password=password, **kwargs)

    def create_issue(self, **kwargs):
        return IssueFactory(**kwargs)

    def sync_permissions(self):
        call_command('sync_permissions', stdout=StringIO())


class AsSuperuserTestCase(object):

    def get_user(self, is_superuser, is_staff=True):
        username = 'user'
        password = 'super secret password'
        email = 'user@test.cz'
        return UserProxy(username, password,
                         User.objects._create_user(username, email, password, is_staff=is_staff,
                                                   is_superuser=is_superuser))
