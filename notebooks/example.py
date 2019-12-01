# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python (meetup-client)
#     language: python
#     name: meetup_client
# ---

import os
import sys

sys.path.append("..")

from dotenv import load_dotenv

from meetup_client.client import MeetupClient

load_dotenv()

meetup_client = MeetupClient(access_token=os.environ["MEETUP_CLIENT_ACCESS_TOKEN"])

(
    meetup_client.get(
        url="pro/pydata/groups",
        member_count_max=100000,
        only="city,country,member_count",
    )
    .sort_values("member_count", ascending=False)
    .head(10)
)

(
    meetup_client.scan(
        url="PyData-Suedwest/members", only="id,group_profile.created"
    ).head()
)
