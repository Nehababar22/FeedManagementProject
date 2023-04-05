from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from users.models import User
        from users.signals import add_default_group
        import users.signals
        
        post_save.connect(add_default_group, sender=User,
                  dispatch_uid="add_default_group")
        
