"""
The Meetup API client.
"""

import math
from time import sleep

import pandas as pd
import requests
from tqdm import tqdm

from .errors import RequestError


class MeetupClient:
    """
    Client for using the Meetup API.

    Args:
        access_token (str): The access token for the API.

    Attributes:
        access_token (str): The access token for the API.
    """

    def __init__(
        self, *, access_token,
    ):
        self.access_token = access_token

    def _get(self, *, url, params, headers=None):
        """
        Runs a GET request against the Meetup API.

        Args:
            url (str): The API route. Must not begin with "https://api.meetup.com/",
                as it is automatically prefixed.
            params (dict): The parameters for the API route.
            headers (dict, optional): The headers for the API route.

        Returns:
            requests.models.Response: The response.

        Raises:
            BadRequestError: If API returns 400.
            UnauthorizedError: If API returns 401.
            TooManyRequestsError: If API returns 429.
            InternalServerError: If API returns 500.
            RequestError: If API returns any other non-200 exit code.
        """
        url = f"https://api.meetup.com/{url}"

        headers = headers or {}
        headers["Authorization"] = (
            headers.get("Authorization") or f"Bearer {self.access_token}"
        )

        res = requests.get(url=url, headers=headers, params=params)

        status_code = res.status_code
        if not str(status_code).startswith("2"):
            raise RequestError(status_code, res)
        return res

    @staticmethod
    def _get_total_count(response):
        """
        Gets the total number of retrievable elements from a response.

        Args:
            response (requests.models.Response): A response.

        Returns:
            int: The total count of retrievable elements.
        """
        return int(response.headers["X-Total-Count"])

    def _scan(self, *, url, params=None, sleep_time=0.1):
        """
        Iterator for pagination in API request.

        Args:
            url (str): Route of API to query from.
            params (dict, optional): Parameters for the API request.
            sleep_time (float, optional): Time to pause between requests.

        Yields:
            requests.models.Response: A response.
        """

        params = params or {}
        params["offset"] = params.get("offset") or 0
        params["page"] = params.get("page") or 200

        if not params["offset"]:
            res = self._get(url=url, params=params)
            yield res
            total_count = self._get_total_count(res)
            total_requests = math.ceil(total_count / params["page"])
        for offset in tqdm(range(params["offset"] + 1, total_requests)):
            params["offset"] = offset
            sleep(sleep_time)
            res = self._get(url=url, params=params)
            yield res

    def get(self, *, url, to_df=True, **params):
        """
        Runs GET request against Meetup API.

        Args:
            url (str): The route to request from.
            to_df (boolean, optional): Whether the response body should be converted to
                a pandas DataFrame.
            **params: Additional arguments for request.

        Returns:
            pandas.DataFrame or list: The response.
        """
        element = self._get(url=url, params=params).json()
        if to_df:
            return pd.DataFrame(element)
        return element

    def scan(self, *, url, to_df=True, sleep_time=0.1, **params):
        """
        Runs GET requests against Meetup API with pagination and returns all pages.

        Args:
            url (str): The route to request from.
            to_df (boolean, optional): Whether the response body should be converted to
                a pandas DataFrame.
            sleep_time (float, optional): Time to pause between requests.
            **params: Additional arguments for request.

        Returns:
            pandas.DataFrame or list: The response.
        """
        responses = self._scan(url=url, sleep_time=sleep_time, params=params)
        elements = [element for response in responses for element in response.json()]
        if to_df:
            return pd.DataFrame(elements)
        return elements
