import requests
import time

from oxford_api import OxfordApi


class OxfordApiV1(OxfordApi):
    def __init__(
            self,
            application_id,
            application_key,
            request_timeout_milliseconds=10000,
            request_interval_milliseconds=300):

        assert application_id != "", "Non empty app_id"
        assert application_key != "", "Non empty app_key"

        self.application_id = application_id
        self.application_key = application_key
        self.request_timeout_milliseconds = request_timeout_milliseconds
        self.request_interval_milliseconds = request_interval_milliseconds
        self.api_root = 'https://od-api.oxforddictionaries.com:443/api/v1/entries'

        # Oxford requires that keys in the header dictionary are called app*,
        # therefore I chose to call API object members accordingly. Sorry if this is confusing.
        self.headers = {'app_id': application_id, 'app_key': application_key}
        self.session = requests.Session()
        self.session.headers = {'application': 'PythonWrapper'}

    def send_request(self, lang, path, method='GET'):
        """Make a GET request to the API"""
        time.sleep(self.request_interval_milliseconds)
        full_uri = self.api_root + '/' + lang + '/' + path
        response = self.session.request(
            method,
            full_uri,
            timeout=self.request_timeout_milliseconds,
            headers=self.headers)

        return response

    def get_synonyms(self, word):
        """
            Get synonyms for chosen word.
        """

        try:
            path = "{}/synonyms".format(word.lower())
            return self.send_request(path)
        except:
            return "No synonyms for {} in our current dictionaries.".format(word)

    def get_antonyms(self, word):
        """
            Get antonyms for chosen word.
        """

        try:
            path = "{}/antonyms".format(word.lower())
            return self.send_request(path)
        except:
            return "No antonyms for {} in our current dictionaries.".format(word)

    def translate(self, word, target_language='es'):
        """
            Get Translation for word from source language
            to target language. Spanish default.
        """

        path = "{}/translations={}".format(word.lower(), target_language)
        return self.send_request(path)

    def get_info_about_word(self, word):
        """
            Get dictionary information for chosen word.
        """

        path = "{}".format(word.lower())
        return self.send_request(path)

    def use_in_sentence(self, word):
        """
            Examples of how to use word in sentence.
        """

        path = "{}/sentences".format(word.lower())
        return self.send_request(path)
