"""
Custom erros for the meetup-api package.
"""


class MeetupApiError(Exception):
    """
    Generic base error for this package.
    """


class AccessTokenError(MeetupApiError):
    """
    Is thrown when access token request contains error message.
    """


class RequestError(MeetupApiError):
    """
    Generic error for requests.
    """

    def __init__(self, description, response=None):
        super().__init__(description)
        self.response = response


class BadRequestError(RequestError):
    """
    400.
    """

    def __init__(self, response):
        super().__init__("There was a problem with the request.", response)


class UnauthorizedError(RequestError):
    """
    401.
    """

    def __init__(self, response):
        super().__init__("You did not provide a valid token.", response)


class TooManyRequestsError(RequestError):
    """
    429.
    """

    def __init__(self, response):
        super().__init__("You have gone over the request rate limit.", response)


class InternalServerError(RequestError):
    """
    500.
    """

    def __init__(self, response):
        super().__init__("An unexpected error occured on the servers.", response)
