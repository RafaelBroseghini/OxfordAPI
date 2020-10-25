from oxforddictionaries.caching_language_dictionary import CachingLanguageDictionary
from oxforddictionaries.credentials import APPLICATION_ID, APPLICATION_KEY
from oxforddictionaries.oxford_api_v2 import OxfordApiV2

if __name__ == "__main__":
    oxford_api = OxfordApiV2(APPLICATION_ID, APPLICATION_KEY)
    caching_language_dictionary = CachingLanguageDictionary(oxford_api, 'en-gb')
    result = caching_language_dictionary.get_definitions("staple")
    print(result)


