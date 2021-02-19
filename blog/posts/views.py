# Packages
from .models import Posts
from datetime import datetime
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Modules
from util import Util
from .usecases import UseCases


@csrf_exempt
def posts(request):
    if request.method == 'GET':
        params = request.GET
        result = UseCases.get_posts(params)

        return JsonResponse(result)

    elif request.method == 'POST':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.create_post(body)

        return JsonResponse(result)

    elif request.method == 'PUT':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.update_post(body)

        return JsonResponse(result)

    elif request.method == 'DELETE':
        body = Util.convert_to_dict(request.body.decode())
        result = UseCases.delete_post(body)

        return JsonResponse(result)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Request Method not Allowed'
        })


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        file = request.FILES['file']
        result = UseCases.upload_image(file)

        return JsonResponse(result)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed only POST Requests'
        })
