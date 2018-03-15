from django.apps import apps


def get_iscore_class_str(cls):
    resource = cls.__module__
    app_config = apps.get_containing_app_config(resource)
    return '{app_label}.{resource}'.format(
        app_label=app_config.label,
        resource=resource,
    )
