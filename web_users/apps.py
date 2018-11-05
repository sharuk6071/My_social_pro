from django.apps import AppConfig


class WebUsersConfig(AppConfig):
    name = 'web_users'

    def ready(self):
        import users.signals
