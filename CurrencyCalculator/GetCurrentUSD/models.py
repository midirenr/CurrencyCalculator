from datetime import datetime

from django.db import models


class CurrencyHistoryUSD(models.Model):
    time = models.TimeField()
    value_in_rubles = models.FloatField()

    @classmethod
    def set_new_value(cls, value: float) -> None:
        current_time = datetime.now().time().replace(microsecond=0)
        cls(time=current_time, value_in_rubles=value).save()

    @classmethod
    def get_latest_values_in_rubles(cls):
        return cls.objects.all().order_by('-time')[:10]
