from django.test import TestCase, Client

from django_perms_iscore.utils import get_iscore_class_str

from articles.cores import ArticlePermUIRESTModelISCore

from .factories import UserFactory, GroupFactory


class ArticleTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client = Client()

    def _get_core_str(self):
        return get_iscore_class_str(ArticlePermUIRESTModelISCore)


class ArticleUserPermTestCase(ArticleTestCase):
    pass


class ArticleGroupPermTestCase(ArticleTestCase):

    def setUp(self):
        super().setUp()
        self.group = GroupFactory()
