from twilio.rest import Client
from data_q import qoutes
from twilio.http.http_client import TwilioHttpClient
import datetime
import os
import random

now = datetime.datetime.now()
print(now)
day = now.day
print(day)
SID = "ACa6da687c16659fa0393e1893af03199c"
AUTH = "5ca10aa07e8247260099862da820d081"

if day == 1 or day == 15:
    sent_q = random.choice(qoutes)
    qoutes.remove(sent_q)
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(SID, AUTH, http_client=proxy_client)
    message = client.messages.create(
        body=f"{sent_q}",
        from_="+1909403 4209",
        to="+97336446029"
    )

