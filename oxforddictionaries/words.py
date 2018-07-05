from api import API

class OxfordDictionaries(API):

    def __init__(self, app_id, app_key, format_='json', language='en', timeout=5, sleep_time=1.5):
        super().__init__(app_id, app_key, language, timeout, sleep_time)
        self.api_root = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + self._LANGUAGE + '/'

    def get_synonyms(self, word):
        """
            Get synonyms for chosen word.
        """
        try:
            path = "{}/synonyms".format(word.lower())
            return self._make_request(path)
        except:
            return "No synonyms for {} in our current dictionaries.".format(word)

    def get_antonyms(self, word):
        """
            Get antonyms for chosen word.
        """
        try:
            path = "{}/antonyms".format(word.lower())
            return self._make_request(path)
        except:
            return "No antonyms for {} in our current dictionaries.".format(word)
    
    def translate(self, word, target_language='es'):
        """
            Get Translation for word from source language
            to target language. Spanish default.
        """

        path = "{}/translations={}".format(word.lower(), target_language)
        return self._make_request(path)

    def get_info_about_word(self, word):
        """
            Get dictionary information for chosen word.
        """

        path = "{}".format(word.lower())
        return self._make_request(path)

    def use_in_sentence(self, word):
        """
            Examples of how to use word in sentence.
        """

        path = "{}/sentences".format(word.lower())
        return self._make_request(path)