import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from services import providers
from urllib.parse import urlencode
from config import deploy
from utils import data_logger
import time

import secrets


def oauth(request):
    params = request.GET
    state = params.get('state', None)
    code = params.get('code', None)
    error = params.get('error', None)
    return JsonResponse({"online": True, "received_params": params})


def gen_auth_url(request):
    service = 'omron'
    provider_info = providers.info[service]
    client_state = secrets.token_urlsafe(16)

    if deploy.PRODUCTION:
        url = provider_info['prod_oauth_server']
    else:
        url = provider_info['dev_oauth_server']

    if url[-1]=='/':
        url=url[:-1]

    url_params = {
        "client_id": provider_info['client_id'],
        "response_type": "code",
        "scope": provider_info['scope'],
        "redirect_uri": provider_info['redirect_uri'],
        "state": client_state
    }

    return JsonResponse({"url" : f'{url}/connect/authorize?{urlencode(url_params)}'})


def get_auth_tokens():
    pass


# For test purpose only
@csrf_exempt
def update_reading(request):
    if request.method != 'POST':
        return JsonResponse({"success": False, "message": "Method not allowed"})
    else:
        data = json.loads(request.body)
        data_logger.log([time.time(), json.dumps(data)])
        return JsonResponse({"success": True})
