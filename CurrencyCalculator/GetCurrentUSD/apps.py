from django.apps import AppConfig


class GetcurrentusdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GetCurrentUSD'

    def ready(self):
        from GetCurrentUSD import scheduler
        scheduler.add_currency_usd_job()
