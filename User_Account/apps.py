from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "User_Account"

    # Connecting & working with signals
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import user_signals
