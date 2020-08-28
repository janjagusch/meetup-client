"""
Tests for the .scan method in meetup_client.client.MeetupClient.
"""

import inspect

import pandas as pd
import pytest

from meetup.client.errors import RequestError


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("PyData-Suedwest/members", {"only": "id,group_profile.created"})]
)
def test_scan_1(meetup_client, url, kwargs):
    assert inspect.isgeneratorfunction(meetup_client.scan)
    res = list(meetup_client.scan(url=url, to_df=True, **kwargs))
    assert isinstance(res[0], pd.DataFrame)


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("PyData-Suedwest/members", {"only": "id,group_profile.created"})]
)
def test_scan_2(meetup_client, url, kwargs):
    assert inspect.isgeneratorfunction(meetup_client.scan)
    res = list(meetup_client.scan(url=url, to_df=False, **kwargs))
    assert isinstance(res[0], list)
    assert isinstance(res[0][0], dict)


@pytest.mark.vcr()
@pytest.mark.parametrize("url,kwargs", [("PyData-Suedwest/members", {})])
def test_scan_unauthorized(meetup_client_invalid, url, kwargs):
    with pytest.raises(RequestError):
        meetup_client_invalid.scan(url=url, **kwargs)
