# Packages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UseCases:
    @staticmethod
    def sign_in(body: dict) -> dict:
        """
        Sign In

        Args:
            body: request body

        Returns:
            dict: result of request
        """
        try:
            username = body.get('username')
            password = body.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                return {
                    'status': True,
                    'message': 'Sign In Successful'
                }

            else:
                return {
                    'status': False,
                    'message': 'Username or Passoword is Incorrect'
                }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while signing in: {e}'
            }

    @staticmethod
    def sign_up(body: dict) -> dict:
        """
        Sign Up

        Args:
            body: request body

        Returns:
            dict: result of request
        """
        try:
            first_name = body['firstName']
            last_name = body['lastName']
            username = body['username']
            password = body['password']
            email = body['email']

            user = User.objects.filter(username=username).exists()
            if user:
                return {
                    'status': True,
                    'message': 'User Already Exists'
                }

            user = User.objects.create_user(
                username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            return {
                'status': True,
                'message': 'Sign up Successful'
            }

        except Exception as e:
            return {
                'status': False,
                'message': f'Error occured while signing up: {e}'
            }
