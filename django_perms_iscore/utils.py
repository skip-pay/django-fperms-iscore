from django.apps import apps


def get_iscore_class_str(cls):
    app_config = apps.get_containing_app_config(cls.__module__)
    core = cls.__name__
    return '{app_label}.{core}'.format(
        app_label=app_config.label,
        core=core,
    )
