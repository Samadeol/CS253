from django.apps import AppConfig


class EmailerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Emailer'

    def ready(self):
        # scheduling emailing
        from . import updater
        updater.start()