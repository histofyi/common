from common.providers import httpProvider



import logging
import json




class PMCeProvider():

    def fetch(self, doi, result_type='core'):
        url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={doi}&format=json&resultType={result_type}'
        try:
            results = httpProvider().get(url, format='json')
        except:
            results = None
        if results:
            results = results['resultList']['result']
            if len(results) > 0:
                results = results[0]
            return results, True, None
        else:
            return None, False, ['unable_to_retrieve']




