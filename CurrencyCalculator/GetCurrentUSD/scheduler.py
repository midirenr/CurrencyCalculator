from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from .views import update_currency_usd


def add_currency_usd_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_currency_usd, trigger=IntervalTrigger(seconds=10))
    scheduler.start()
