import util
from oxford_api import OxfordApi


class CachingLanguageDictionary:
    def __init__(
            self,
            oxford_api: OxfordApi,
            language='en-gb',
            cached_words_path='oxford_cached_words.json',
            bad_words_path='bad_words.json',
            query_limit=50):
        self.oxford_api = oxford_api
        self.language = language
        self.cached_words_path = cached_words_path
        self._read_cached_results()
        self.bad_words_path = bad_words_path
        self._read_bad_words()
        self.query_limit = query_limit

    def __del__(self):
        self._write_bad_words()
        self._write_cached_results()

    def get_definitions(self, word):
        if not self._is_query_within_limit():
            print("ERROR: Exceeded query limit :(")
            return None

        if word in self.cached_results:
            print(f"Word '{word}' was cached. Not querying the API and returning cached result.")
            return self.cached_results[word]

        entries = self.oxford_api.get_entries(self.language, word)
        entries_json = entries.json()

        if 'results' not in entries_json:
            print(f"Word '{word}' not found. Adding to bad words.")
            self.bad_words.add(word)
            return None

        print(f"Word '{word}' found. Caching result.")
        results = entries_json['results']
        self.cached_results[word] = results
        return results

    def _read_cached_results(self):
        try:
            self.cached_results = util.read_json(self.cached_words_path)
        except Exception:
            print("Could not locate {}. Using empty cached results.".format(self.cached_words_path))
            self.cached_results = dict()

    def _write_cached_results(self):
        util.dump_json(self.cached_results, self.cached_words_path)

    def _read_bad_words(self):
        try:
            self.bad_words = set(util.read_json(self.bad_words_path))
        except:
            print("Could not locate {}. Using empty bad words".format(self.bad_words_path))
            self.bad_words = set()

    def _write_bad_words(self):
        util.dump_json(list(self.bad_words), self.bad_words_path)

    def _is_query_within_limit(self):
        if self.query_limit <= 0:
            return False

        self.query_limit -= 1
        if self.query_limit <= 0:
            return False

        return True
