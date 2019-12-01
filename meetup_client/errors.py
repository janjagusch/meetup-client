"""
Custom erros for the meetup-api package.
"""


class MeetupApiError(Exception):
    """
    Generic base error for this package.
    """


class RequestError(MeetupApiError):
    """
    Generic error for requests.
    """

    def __init__(self, status_code, response=None):
        super().__init__(status_code)
        self._response = response
