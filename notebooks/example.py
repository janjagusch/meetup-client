# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python (meetup-client)
#     language: python
#     name: meetup_client
# ---

import os
import sys

sys.path.append("..")

from dotenv import load_dotenv
import pandas as pd

from meetup.client import Client

load_dotenv()

client = Client(access_token=os.environ["MEETUP_CLIENT_ACCESS_TOKEN"])

(
    pd.concat(client.scan(url="PyData-Suedwest/members", only="id,city"))
    .groupby("city")
    .size()
    .sort_values(ascending=False)
    .head(10)
)
