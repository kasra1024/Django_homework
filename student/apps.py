from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'

    def ready(self):
        from . import signals