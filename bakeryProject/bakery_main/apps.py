from django.apps import AppConfig


class BakeryMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakeryProject.bakery_main'

    def ready(self):
        import bakeryProject.bakery_main.signals
        result = super().ready()
        return result
