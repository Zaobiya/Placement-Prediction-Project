from django.apps import AppConfig


class AimzConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aimz'

    def ready(self):
        import aimz.signals