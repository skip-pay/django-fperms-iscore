from is_core.main import DjangoUiRestCore

from fperms_iscore.mixins import PermCoreMixin


class PermDjangoUiRestCore(PermCoreMixin, DjangoUiRestCore):
    """
    Primary Core class for production Django model administration.

    Combines UI and REST functionality with automatic permission management.
    Recommended for most production use cases without advanced features.
    """

    abstract = True
