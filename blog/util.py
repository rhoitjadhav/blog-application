""" This Class contains helper functions """

import json


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
