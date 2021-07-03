from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_app_config = 'django.db.models.BigAutoField'
    name = 'bookingvisit'

    def ready(self):
        from bookingvisit import signals