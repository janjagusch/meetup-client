import pandas as pd
import pytest

from meetup_client.errors import RequestError


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("PyData-Suedwest/members", {"only": "id,group_profile.created"})]
)
def test_scan_1(meetup_client, url, kwargs):
    res = meetup_client.scan(url=url, to_df=True, **kwargs)
    assert isinstance(res, pd.DataFrame)


@pytest.mark.vcr()
@pytest.mark.parametrize(
    "url,kwargs", [("PyData-Suedwest/members", {"only": "id,group_profile.created"})]
)
def test_scan_2(meetup_client, url, kwargs):
    res = meetup_client.scan(url=url, to_df=False, **kwargs)
    assert isinstance(res, list)


@pytest.mark.vcr()
@pytest.mark.parametrize("url,kwargs", [("PyData-Suedwest/members", {})])
def test_scan_unauthorized(meetup_client_invalid, url, kwargs):
    with pytest.raises(RequestError):
        res = meetup_client_invalid.scan(url=url, **kwargs)
