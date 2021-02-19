# Packages
from django.contrib.auth.models import User

# Modules
from .models import Followers, Following


class UseCases:
    @staticmethod
    def get_followers(params: dict) -> dict:
        """
        Get Followers list

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

            data = []
            followers = Followers.objects.filter(user_id=user.id).all()
            for follower in followers:
                user = User.objects.get(id=follower.follower_id)
                data.append({
                    "username": user.username,
                    'first_name': user.first_name,
                    "last_name": user.last_name,
                    "email": user.email
                })

            return {
                'status': True,
                'message': 'Data found',
                'data': data
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error while getting followers list: {e}'
            }

    @staticmethod
    def add_follower(body: dict) -> dict:
        """
        Add Follower

        Args:
            body: request body

        Returns:
            dict: result of request
        """
        try:
            follower_username = body['followerUsername']
            username = body['username']

            follower = User.objects.filter(username=follower_username).first()
            if follower is None:
                return {
                    'status': False,
                    'message': 'Follower not found'
                }

            user = User.objects.filter(username=username).first()
            if user is False:
                return {
                    'status': False,
                    'message': 'User not found'
                }

            follower = Followers(follower_id=follower.id, user=user)
            follower.save()

            return {
                'status': True,
                'message': 'Follower added'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while adding follower: {e}'
            }

    @staticmethod
    def delete_follower(body: dict) -> dict:
        """
        Delete Follower

        Args:
            body: request body

        Returns:
            dict: result of request
        """
        try:
            follower_username = body['followerUsername']
            username = body['username']

            follower = User.objects.filter(username=follower_username).first()
            if follower is False:
                return {
                    'status': False,
                    'message': 'Follower not found'
                }

            user = User.objects.filter(username=username).first()
            if user is False:
                return {
                    'status': False,
                    'message': 'User not found'
                }

            follower = Followers.objects.filter(
                follower_id=follower.id, user_id=user.id)
            follower.delete()

            return {
                'status': True,
                'message': 'Follower deleted'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while deleting follower: {e}'
            }

    @staticmethod
    def get_following(params: dict) -> dict:
        """
        Get Following list

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

            data = []
            followings = Following.objects.filter(user_id=user.id).all()
            for following in followings:
                user = User.objects.get(id=following.following_id)
                data.append({
                    "username": user.username,
                    'first_name': user.first_name,
                    "last_name": user.last_name,
                    "email": user.email
                })

            return {
                'status': True,
                'message': 'Data found',
                'data': data
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error while getting following list: {e}'
            }

    @staticmethod
    def add_following(body: dict) -> dict:
        """
        Add Following

        Args:
            body: request body

        Returns:
            dict: result of request
        """
        try:
            following_username = body['followingUsername']
            username = body['username']

            following = User.objects.filter(
                username=following_username).first()
            if following is None:
                return {
                    'status': False,
                    'message': 'Following not found'
                }

            user = User.objects.filter(username=username).first()
            if user is False:
                return {
                    'status': False,
                    'message': 'User not found'
                }

            following = Following(following_id=following.id, user=user)
            following.save()

            return {
                'status': True,
                'message': 'Following added'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while adding following: {e}'
            }

    @ staticmethod
    def delete_following(body: dict) -> dict:
        """
        De;ete Following

        Args:
            body: request body

        Returns:
            dict: result of request
        """
        try:
            following_username = body['followingUsername']
            username = body['username']

            following = User.objects.filter(
                username=following_username).first()
            if following is False:
                return {
                    'status': False,
                    'message': 'Following not found'
                }

            user = User.objects.filter(username=username).first()
            if user is False:
                return {
                    'status': False,
                    'message': 'User not found'
                }

            following = Following.objects.filter(
                following_id=following.id, user_id=user.id)
            following.delete()

            return {
                'status': True,
                'message': 'Following deleted'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while deleting following: {e}'
            }
