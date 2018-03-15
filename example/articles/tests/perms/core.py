from django_perms_iscore import enums
from django_perms_iscore.exceptions import IsCoreDoesNotExist
from django_perms_iscore.models import IsCorePerm

from .base import ArticleTestCase, ArticleUserPermTestCase


class CorePermTestCaseMixin:

    def _create_perm(self):
        return self._create_read_perm()

    def _create_read_perm(self):
        return IsCorePerm.objects.create(
            type=enums.PERM_TYPE_CORE,
            codename='read',
            core=self._get_core_str()
        )

    def _create_wildcard_perm(self):
        return IsCorePerm.objects.create(
            type=enums.PERM_TYPE_CORE,
            codename=enums.PERM_CODENAME_WILDCARD,
            core=self._get_core_str()
        )


class CorePermTestCase(CorePermTestCaseMixin, ArticleTestCase):

    def test_perm_has_correct_type(self):
        perm = self._create_perm()
        self.assertTrue(perm.is_core_perm())


class ArticleUserModelPermPermTestCase(CorePermTestCase, ArticleUserPermTestCase):

    def test_add_core_perm_by_perm(self):
        perm = self._create_perm()

        self.user.perms.add(perm)

        self.assertTrue(self.user.perms.has_perm(perm))

    def test_add_core_perm_by_str(self):
        read_perm = self._create_read_perm()

        self.user.perms.add('core.articles.ArticlePermUIRESTModelISCore.read')

        self.assertTrue(self.user.perms.has_perm(read_perm))

    def test_fail_add_core_perm_by_non_existent_codename(self):
        self._create_perm()
        with self.assertRaises(IsCorePerm.DoesNotExist):
            self.user.perms.add('core.articles.ArticlePermUIRESTModelISCore.delete')

    def test_fail_add_core_perm_by_non_existent_core(self):
        self._create_perm()
        with self.assertRaises(IsCoreDoesNotExist):
            self.user.perms.add('core.articles.Bar.read')

    def test_has_core_perm_from_wildcard(self):
        self._create_wildcard_perm()

        self.user.perms.add('core.articles.ArticlePermUIRESTModelISCore.*')

        self.assertTrue(self.user.perms.has_perm('core.articles.ArticlePermUIRESTModelISCore.whatever'))
    #
    # def test_core_url_access_rights(self):
    #     print(self.client.get('/articles/'))
