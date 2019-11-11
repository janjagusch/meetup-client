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

import os

import dotenv

dotenv.load_dotenv()

from meetup_api.client import MeetupClient

meetup_client = MeetupClient(
    consumer_key=os.environ["MEETUP_CONSUMER_KEY"],
    consumer_secret=os.environ["MEETUP_CONSUMER_SECRET"],
    redirect_uri=os.environ["MEETUP_CONSUMER_REDIRECT_URI"],
    access_token=os.environ["MEETUP_CONSUMER_ACCESS_TOKEN"],
)

meetup_client.get(
    url="pro/pydata/groups", member_count_max=100000, only="city,country,member_count"
).sort_values("member_count", ascending=False).head(10)

meetup_client.get(url="PyData-Suedwest/similar_groups")

type(requests.get("https://www.google.com"))

meetup_client.get(url="/find/groups", zip="69123", country="Germany").sort_values(
    "members", ascending=False
)[["name", "city", "members"]].head(20).reset_index(drop=True)

meetup_client.get(
    url="/PyData-Suedwest/members", to_df=True, only="id,name", page=10, offset=0
)

meetup_client.scroll(
    url="PyData-Suedwest/members", only="id,name,group_profile.created",
)

# https://www.meetup.com/meetup_api/auth/#oauth2
# https://www.meetup.com/meetup_api/docs/#v3_json
