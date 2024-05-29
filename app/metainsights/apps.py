from django.apps import AppConfig


class MetainsightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metainsights'

    def ready(self):
        import metainsights.signals