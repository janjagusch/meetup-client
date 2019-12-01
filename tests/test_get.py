import pandas as pd
import pytest

from meetup_client.errors import RequestError


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("pro/pydata/groups", {"only": "city,country,member_count"})]
)
def test_get_1(meetup_client, url, kwargs):
    res = meetup_client.get(url=url, to_df=True, **kwargs)
    assert isinstance(res, pd.DataFrame)


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("pro/pydata/groups", {"only": "city,country,member_count"})]
)
def test_get_2(meetup_client, url, kwargs):
    res = meetup_client.get(url=url, to_df=False, **kwargs)
    assert isinstance(res, list)


@pytest.mark.vcr()
@pytest.mark.parametrize("url,kwargs", [("pro/pydata/groups", {})])
def test_get_unauthorized(meetup_client_invalid, url, kwargs):
    with pytest.raises(RequestError):
        res = meetup_client_invalid.get(url=url, **kwargs)
