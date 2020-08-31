"""
Tests for the .get method in meetup_client.client.MeetupClient.
"""


import pandas as pd
import pytest

from meetup.client.errors import RequestError


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("PyData-Suedwest/events", {"status": "past"}),]
)
def test_get_1(meetup_client, url, kwargs):
    res = meetup_client.get(url=url, to_df=True, **kwargs)
    assert isinstance(res, pd.DataFrame)


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("PyData-Suedwest/events", {"status": "past"}),]
)
def test_get_2(meetup_client, url, kwargs):
    res = meetup_client.get(url=url, to_df=False, **kwargs)
    assert isinstance(res, list)


@pytest.mark.vcr()
@pytest.mark.parametrize("url,kwargs", [("PyData-Suedwest/events", {}),])
def test_get_unauthorized(meetup_client_invalid, url, kwargs):
    with pytest.raises(RequestError):
        meetup_client_invalid.get(url=url, **kwargs)
