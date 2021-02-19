# Packages
import os
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile

# Modules
from util import Util
from .models import Posts
from follow.models import Following


class UseCases:
    @staticmethod
    def upload_image(file: InMemoryUploadedFile) -> dict:
        """
        Upload image file

        Args:
            file: InMemoryUploadedFile object which contains file related data

        Returns:
            dict: result of request
        """
        try:
            filename = Util.generate_string() + '.' + \
                (file.name).split('.')[-1]
            file_path = os.path.join(
                settings.FILE_STORAGE_ROOT, filename)

            Util.save_to_file(file, file_path)

            return {
                'status': True,
                'message': 'File Uploaded Successfully',
                'data': os.path.basename(file_path)
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error while uploading file: {e}',
            }

    @staticmethod
    def get_posts(params: dict) -> dict:
        """
        Get list of posts which user has followed

        Args:
            params: request url parameters

        Returns:
            dict: result of request        

        """
        try:
            username = params['username']
            user = User.objects.filter(username=username).first()
            if user is None:
                return {
                    'status': False,
                    'message': 'User not found'
                }

            followings = Following.objects.filter(user_id=user.id).all()

            data = []
            for following in followings:
                posts = Posts.objects.filter(
                    user_id=following.following_id).all()
                for post in posts:
                    data.append({
                        "postId": post.id,
                        "content": post.content,
                        "createTime": post.create_time,
                        "updateTime": post.update_time,
                        "image": post.image
                    })

            return {
                'status': True,
                'message': 'Data Found',
                'data': data
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while getting posts list: {e}'
            }

    @staticmethod
    def create_post(body: dict) -> dict:
        """
        Create Post

        Args:
            body: request body

        Returns:
            dict: result of request        

        """
        try:
            content = body['content']
            username = body['username']
            image = body['image']
            create_time = update_time = timezone.now()

            user = User.objects.filter(username=username).exists()
            if user is False:
                return {
                    'status': False,
                    'message': 'User is not created'
                }

            post = Posts(content=content, create_time=create_time,
                         update_time=update_time, image=image, user=User.objects.get(username=username))

            post.save()

            return {
                'status': True,
                'message': 'Posts Created Successfully'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while adding posts list: {e}'
            }

    @staticmethod
    def update_post(body: dict) -> dict:
        """
        Update Post

        Args:
            body: request body

        Returns:
            dict: result of request

        """
        try:
            post_id = body['postId']
            content = body['content']
            update_time = timezone.now()

            post = Posts.objects.filter(id=post_id).first()
            if post is False:
                return {
                    'status': False,
                    'message': 'Post is not created'
                }

            post.content = content
            post.update_time = update_time
            post.save()

            return {
                'status': True,
                'message': 'Post updated successfully'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while updating posts list: {e}'
            }

    @staticmethod
    def delete_post(body: dict) -> dict:
        """
        Delete Post

        Args:
            body: request body

        Returns:
            dict: result of request        

        """
        try:
            post_id = body['postId']

            post = Posts.objects.filter(id=post_id).first()
            if post is False:
                return {
                    'status': False,
                    'message': 'Post is not created'
                }

            post.delete()

            return {
                'status': True,
                'message': 'Post deleted successfully'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while deleting posts list: {e}'
            }
