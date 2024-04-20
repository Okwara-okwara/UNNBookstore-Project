from django.apps import AppConfig


class UnnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Unnapp'

    def ready(self):
        import Unnapp.signals