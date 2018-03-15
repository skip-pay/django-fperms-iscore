from django.contrib.auth import get_user_model

from germanium.test_cases.auth import UserProxy

from is_core.tests import crawler

from articles.tests.perms.factories import UserFactory, DEFAULT_PASSWORD

from django_perms import get_perm_model


class CrawlerTestCase(crawler.CrawlerTestCase):

    def set_up(self):
        self.user = UserFactory()
        perm = get_perm_model().objects.create_from_str('core.articles.ArticlePermUIRESTModelISCore.read')
        self.user.perms.add(perm)

    def get_user(self):
        user = UserFactory()
        return UserProxy(user.username, DEFAULT_PASSWORD, self.get_user_obj(user.username))

    def get_users(self):
        return [self.get_user()]

    def get_user_obj(self, username):
        return get_user_model().objects.get(username=username)
