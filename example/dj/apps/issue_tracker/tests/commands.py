from io import StringIO

from django.core.management import call_command

from germanium.test_cases.default import GermaniumTestCase
from germanium.tools import assert_equal, assert_false

from fperms.models import Perm

from fperms_iscore.enums import PERM_TYPE_CORE


class CommandsTestCase(GermaniumTestCase):

    def test_permissions_should_be_synchronized(self):
        assert_false(Perm.objects.exists())
        call_command('sync_permissions', stdout=StringIO())
        assert_equal(Perm.objects.count(), 12)

        model_names = {'user', 'issue', 'group'}
        perm_names = {'create', 'read', 'update', 'delete'}

        for model_name in model_names:
            for perm_name in perm_names:
                assert_equal(
                    Perm.objects.filter(type=PERM_TYPE_CORE, codename='{}__{}'.format(model_name, perm_name)).count(), 1
                )
