from typing import Dict, List, Tuple
import json


import requests


class plausibleProvider():

    def __init__(self, domain:str):
        self.url = 'https://plausible.io/api/event'
        self.domain = domain


    def empty_search(self, query:str) -> Tuple[Dict, bool, List]:
        errors = []
        search_url = f'https://www.histo.fyi/search?query={query}'
        payload = {'name': 'EmptySearch', 'domain': 'histo.fyi','url':search_url,'props':{'query':query}}
        headers = {'Content-type': 'application/json'}
        r = requests.post(self.url, data=json.dumps(payload), headers=headers)
        if r.status_code == 200:
            return {'return':r.content}, True, errors
        else:
            return {'return':r.content}, False, ['plausible_errors']
