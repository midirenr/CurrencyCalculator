from django.http import JsonResponse
import requests

from .models import CurrencyHistoryUSD


def get_currency_usd(request):
    data = CurrencyHistoryUSD.get_latest_values_in_rubles()
    data_list = [data for data in data.values('time', 'value_in_rubles')]
    return JsonResponse(data_list, safe=False)


def update_currency_usd():
    """
    Обновить валюту USD

    Описание: функция для джобы, которая автоматически запускается каждые 10 секунд.
    """
    response = requests.get(url="https://openexchangerates.org/api/latest.json?"
                                "app_id=86dc21712965404094a31edb8bbd0251&"
                                "base=USD&"
                                "symbols=RUB")
    rub_in_usd = float(response.json()['rates']['RUB'])
    CurrencyHistoryUSD.set_new_value_in_rubles(value=rub_in_usd)
