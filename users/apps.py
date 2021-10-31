from django.apps import AppConfig 
#this is a config file


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
