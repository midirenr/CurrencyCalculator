from datetime import datetime

from django.http import JsonResponse


def get_currency_usd(request):
    data = {'time': datetime.now().time().strftime('%H:%M:%S')}
    return JsonResponse(data)


def update_currency_usd():
    print(datetime.now().time().strftime('%H:%M:%S'))
