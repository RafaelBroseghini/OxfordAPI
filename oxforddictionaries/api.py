import requests
import time
import json

class API(object):

    session = requests.Session()
    session.headers = {'application': 'PythonWrapper'}

    def __init__(self, app_id, app_key, language='en', timeout=5, sleep_time=1.5):
        assert app_id != "", "Non empty app_id"
        assert app_key != "", "Non empty app_key"

        # Oxford requires that keys in the header dictionary are called app*, 
        # therefore I chose to call API object members accordingly. Sorry if this is confusing.

        self.headers = {'app_id': app_id,'app_key': app_key}
        self._LANGUAGE = language
        self.timeout = timeout
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET'):
        """Make a GET request to the API"""
        time.sleep(self._sleep_time)  # Rate limiting
        full_uri = self.api_root + path 
        response = self.session.request(method,
                                        full_uri,
                                        timeout=self.timeout,
                                        headers=self.headers)
        return response