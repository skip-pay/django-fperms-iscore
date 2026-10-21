from django.db import transaction
from django.db.models.signals import m2m_changed, post_delete

from fperms import get_perm_model
from fperms.models import Group

from fperms_iscore.permissions import invalidate_perm_cache


def _invalidate_perm_cache_on_commit():
    # On commit, so that a concurrent request cannot cache the old permissions under the new version.
    transaction.on_commit(invalidate_perm_cache)


def _m2m_changed(action, **kwargs):
    if action.startswith('post_'):
        _invalidate_perm_cache_on_commit()


def _post_delete(**kwargs):
    _invalidate_perm_cache_on_commit()


def connect_signals():
    Perm = get_perm_model()
    for through in (Perm.users.through, Group.users.through, Group.fperms.through, Group.fgroups.through):
        m2m_changed.connect(_m2m_changed, sender=through)
    for model in (Perm, Group):
        post_delete.connect(_post_delete, sender=model)
