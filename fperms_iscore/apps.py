# -*- coding: utf-8
from django.apps import AppConfig


class FPermsISCoreConfig(AppConfig):
    name = 'fperms_iscore'

    def ready(self):
        from fperms_iscore.signals import connect_signals

        connect_signals()
