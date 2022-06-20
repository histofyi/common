from common.providers import httpProvider



import logging
import json




class rcsbProvider():

    pdb_code = None

    def __init__(self, pdb_code):
        self.pdb_code = pdb_code
        self.url_stem = 'https://data.rcsb.org/rest/v1/core'

    def fetch(self, route, identifier):
        url = f'{self.url_stem}/{route}/{self.pdb_code}/{identifier}'
        results = httpProvider().get(url, format='json')
        if results:
            trimmed_results = results
            return trimmed_results, True, []
        else:
            return {}, False, ['unable_to_fetch']

    def fetch_uniprot(self, identifier):
        return self.fetch('uniprot', identifier)
    
