"""
Helper methods for the tests.
"""

import os

from dotenv import load_dotenv
import pytest

from meetup_client import MeetupClient


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
    The access token for the MeetupClient object.
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
    The MeetupClient object.
    """
    return MeetupClient(access_token=access_token)


@pytest.fixture(name="meetup_client_invalid")
def meetup_client_invalid_(access_token_invalid):
    """
    MeetupClient object with invlaid access token.
    """
    return MeetupClient(access_token=access_token_invalid)
