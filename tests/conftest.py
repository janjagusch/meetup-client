"""
Helper methods for the tests.
"""

import os

import pytest
from dotenv import load_dotenv

from meetup.client import Client


@pytest.fixture(scope="module")
def vcr_config():
    """
    vcr_config.
    """
    return {
        "filter_headers": [("Authorization", "XXX")],
    }


@pytest.fixture(name="vcr", scope="module")
def vcr_(vcr):
    """
    vcr.
    """
    vcr.match_on = ["method", "scheme", "port", "path", "body", "query"]
    return vcr


@pytest.fixture(name="access_token")
def access_token_():
    """
    The access token for the Client object.
    """
    load_dotenv()
    return os.environ.get("MEETUP_CLIENT_ACCESS_TOKEN") or "XXX"


@pytest.fixture(name="access_token_invalid")
def access_token_invalid_():
    """
    An invalid access token.
    """
    return "XXX"


@pytest.fixture(name="meetup_client")
def meetup_client_(access_token):
    """
    The Client object.
    """
    return Client(access_token=access_token)


@pytest.fixture(name="meetup_client_invalid")
def meetup_client_invalid_(access_token_invalid):
    """
    Client object with invlaid access token.
    """
    return Client(access_token=access_token_invalid)
