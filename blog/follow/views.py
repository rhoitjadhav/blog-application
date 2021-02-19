# Packages
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Modules
from util import Util
from .usecases import UseCases


@csrf_exempt
def follower(request):
    if request.method == 'GET':
        params = request.GET
        result = UseCases.get_followers(params)

        return JsonResponse(result)

    elif request.method == 'POST':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.add_follower(body)

        return JsonResponse(result)

    elif request.method == 'DELETE':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.delete_follower(body)

        return JsonResponse(result)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Request Method not Allowed'
        })


@ csrf_exempt
def following(request):
    if request.method == 'GET':
        params = request.GET
        result = UseCases.get_following(params)

        return JsonResponse(result)

    elif request.method == 'POST':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.add_following(body)

        return JsonResponse(result)

    elif request.method == 'DELETE':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.delete_following(body)

        return JsonResponse(result)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Request Method not Allowed'
        })
