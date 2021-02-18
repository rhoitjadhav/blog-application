# Packages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Modules
from util import Util


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        try:
            body = Util.convert_to_dict(request.body.decode())
            username = body.get('username')
            password = body.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                return JsonResponse({
                    'status': True,
                    'message': 'Sign In Successful'
                })

            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Username or Passoword is Incorrect'
                })

        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f'Error occured while signing in: {e}'
            })

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only POST Requests'
        })


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        try:
            body = Util.convert_to_dict(request.body.decode())
            first_name = body['firstName']
            last_name = body['lastName']
            username = body['username']
            password = body['password']
            email = body['email']

            user = User.objects.filter(username=username).exists()
            if user:
                return JsonResponse({
                    'status': True,
                    'message': 'User Already Exists'
                })

            user = User.objects.create_user(
                username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            return JsonResponse({
                'status': True,
                'message': 'Sign up Successful'
            })

        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f'Error occured while signing up: {e}'
            })

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only POST Requests'
        })


@csrf_exempt
def test(request):
    user = User.objects.get(username='rohit')
    return JsonResponse({
        'test': user.id
    })
