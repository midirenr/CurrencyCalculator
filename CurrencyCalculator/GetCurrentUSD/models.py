from datetime import datetime

from django.db import models


class CurrencyHistoryUSD(models.Model):
    """
    time: время получение курса
    value_in_rubles: стоимость доллара в рублях
    """
    time = models.TimeField()
    value_in_rubles = models.FloatField()

    @classmethod
    def set_new_value_in_rubles(cls, value: float) -> None:
        """
        Установить новую стоимость доллара в рублях

        :params value: стоимость USD в рублях
        """
        current_time = datetime.now().time().replace(microsecond=0)
        cls(time=current_time, value_in_rubles=value).save()

    @classmethod
    def get_latest_values_in_rubles(cls):
        """
        Получить последние значения в рублях

        Описание: возвращает queryset с последними 10 записями.
        Записи отсортированы по убыванию времени получения (time)

        :return queryset
        """
        return cls.objects.all().order_by('-time')[:10]
