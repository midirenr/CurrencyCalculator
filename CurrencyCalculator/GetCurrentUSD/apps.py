from django.apps import AppConfig

from .scheduler import add_currency_usd_job


class GetcurrentusdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GetCurrentUSD'

    def ready(self):
        add_currency_usd_job()
