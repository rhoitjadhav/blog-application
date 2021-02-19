# Packages
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Modules
from util import Util
from .usecases import UseCases


@csrf_exempt
def sign_in(request):
    """Sign In"""
    if request.method == 'POST':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.sign_in(body)

        return JsonResponse(result)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only POST Requests'
        })


@csrf_exempt
def sign_up(request):
    """Sign Up"""
    if request.method == 'POST':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.sign_up(body)

        return JsonResponse(result)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only POST Requests'
        })
