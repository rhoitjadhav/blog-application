# Packages
import pytz
from .models import Posts
from datetime import datetime
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Modules
from util import Util


@csrf_exempt
def create(request):
    """Create Posts"""

    if request.method == 'POST':
        try:
            body = Util.convert_to_dict(request.body.decode())
            content = body['content']
            username = body['username']
            create_time = update_time = datetime.now()

            user = User.objects.filter(username=username).exists()
            if user is False:
                return JsonResponse({
                    'status': True,
                    'message': 'User is not created'
                })

            post = Posts(content=content, create_time=create_time,
                         update_time=update_time, user=User.objects.get(username=username))

            post.save()

            return JsonResponse({
                'status': True,
                'message': 'Posts Created Successfully'
            })

        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f'Error occured while creating post: {e}'
            })

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only POST Requests'
        })


@csrf_exempt
def update(request):
    """Update Posts"""

    if request.method == 'PUT':
        try:
            body = Util.convert_to_dict(request.body.decode())
            post_id = body['postId']
            content = body['content']
            update_time = datetime.now()

            post = Posts.objects.filter(id=post_id).exists()
            if post is False:
                return JsonResponse({
                    'status': True,
                    'message': 'Post is not created'
                })

            post = Posts.objects.get(id=post_id)
            post.content = content
            post.update_time = update_time
            post.save()

            return JsonResponse({
                'status': True,
                'message': 'Post updated successfully'
            })

        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f'Error occured while updating post: {e}'
            })

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only PUT Requests'
        })


@csrf_exempt
def delete(request):
    """Delete Posts"""

    if request.method == 'DELETE':
        try:
            body = Util.convert_to_dict(request.body.decode())
            post_id = body['postId']

            post = Posts.objects.filter(id=post_id).exists()
            if post is False:
                return JsonResponse({
                    'status': False,
                    'message': 'Post is not created'
                })

            post = Posts.objects.get(id=post_id)
            post.delete()

            return JsonResponse({
                'status': True,
                'message': 'Post deleted successfully'
            })

        except Exception as e:
            return JsonResponse({
                'status': False,
                'message': f'Error occured while deleting post: {e}'
            })

    else:
        return JsonResponse({
            'status': False,
            'message': 'Allowed Only DELETE Requests'
        })
