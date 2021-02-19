""" This Class contains helper functions """

import json
import random
import string


class Util:
    @staticmethod
    def convert_to_dict(data: str) -> dict:
        """
        Convert json string to python dict

        Args:
            data: json string

        Returns:
            dict: converted json string to dict
        """
        return json.loads(data)

    @staticmethod
    def save_to_file(file_data: bytes, file: str) -> bool:
        """
        Write binary data to file

        Args:
            file_data: binary data
            file: path of file to write the data

        Returns:
            bool: True if data written to file, otherwise False
        """

        with open(file, 'wb+') as fp:
            for chunk in file_data:
                fp.write(chunk)

    @staticmethod
    def generate_string(length: int = 8) -> str:
        """
        Generate alphanumeric random string of specified length default to 8

        Args:
            length: length of string to be return

        Returns:
            str: alphanumeric string 
        """
        return ''.join(random.choice(string.ascii_uppercase +
                                     string.ascii_lowercase + string.digits) for _ in range(length))
