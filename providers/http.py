import requests
import json

import logging



from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=5,
    backoff_factor=0.5,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

#response = http.get("https://en.wikipedia.org/w/api.php")

class httpProvider():

    def get(self, url, format, params=None):
        r = http.get(url)
        if r.status_code == 200:
            if format == 'txt':
                content = r.text
            elif format == 'json':
                content = r.json()
            return content
        else:
            return None


    def post(self, url, payload, format):
        r = requests.post(url, data = payload)
        if r.status_code == 200:
            if format == 'json':
                content = r.json()
            else:
                content = r.text
            return content
        else:
            print (r.status_code)
            print (r.text)
            return None
