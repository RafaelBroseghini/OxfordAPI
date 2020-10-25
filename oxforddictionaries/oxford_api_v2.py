import requests
import time

from oxford_api import OxfordApi


class OxfordApiV2(OxfordApi):
    def __init__(
            self,
            application_id,
            application_key,
            request_timeout_milliseconds=10000,
            request_interval_milliseconds=300):

        assert application_id != "", "Empty application_id"
        assert application_key != "", "Empty application_key"

        self.application_id = application_id
        self.application_key = application_key
        self.request_timeout_milliseconds = request_timeout_milliseconds
        self.request_interval_milliseconds = request_interval_milliseconds
        self.api_root = 'https://od-api.oxforddictionaries.com/api/v2'

        # Oxford requires that keys in the header dictionary are called app*,
        # therefore I chose to call API object members accordingly. Sorry if this is confusing.
        self.headers = {'app_id': application_id, 'app_key': application_key}
        self.session = requests.Session()
        self.session.headers = {'application': 'PythonWrapper'}

    def send_request(self, path, method='GET'):
        """Make a GET request to the API"""
        time.sleep(self.request_interval_milliseconds / 1000)
        full_uri = self.api_root + '/' + path
        response = self.session.request(
            method,
            full_uri,
            timeout=self.request_timeout_milliseconds,
            headers=self.headers)

        return response

    def get_entries(self, lang, word):
        path = f'entries/{lang}/{word.lower()}?fields=definitions&strictMatch=false'
        return self.send_request(path)

