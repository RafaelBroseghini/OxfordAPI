from api import API

class Oxford(API):

    def __init__(self, app_id, app_key, format_='json', language='en', timeout=5, sleep_time=1.5):
        super().__init__(app_id, app_key, language, timeout, sleep_time)
        self.api_root = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + self._LANGUAGE + '/'

    def get_synonyms(self, word):
        """
            Get synonyms for chosen word.
        """
        path = "{}/synonyms".format(word.lower())
        return self._make_request(path)

    def get_antonyms(self, word):
        """
            Get antonyms for chosen word.
        """
        try:
            path = "{}/antonyms".format(word.lower())
            return self._make_request(path)
        except:
            return "No antonyms for {}".format(word)
    
    def get_info_about_word(self, word):
        """
            Get dictionary information for chosen word.
        """

        path = "{}".format(word.lower())
        return self._make_request(path)


# o = Oxford('438eaf0a', 'a19c0ea86179f5be927cf61ac4a391b1')

# # print(o.get_info_about_word("book"))
# relax = o.get_synonyms("absorb")

# synonyms = relax['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']

# for s in range(10):
#     print(synonyms[s]['text'])