from django.apps import AppConfig
from django.conf import settings


class DjangoCmsHelpersConfig(AppConfig):
    name = 'djangocms_helpers'

    # noinspection PyUnresolvedReferences
    def ready(self):
        is_django_cms_installed = 'cms' in settings.INSTALLED_APPS
        if is_django_cms_installed:
            from djangocms_helpers.monkey_patches.static_placeholder_publishing_fix import monkeypatch_cms_has_publish_permission

