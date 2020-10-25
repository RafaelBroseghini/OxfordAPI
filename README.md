# Oxford Dictionary API Python Wrapper

This is a python wrapper around the Oxford Dictionary API.
The Oxford API offers a free plan with up to 3,000 requests per month with full access to Oxford Dictionaries data, although you will need to register for an API key. Sign up [here](https://developer.oxforddictionaries.com/).

In addition to the API wrapper a caching structure is provided for requesting entries from APIv2 and persisting the results such that the API is not queried multiple times for the already checked word.

## Installation

* `git clone git@github.com:RafaelBroseghini/OxfordAPI.git`
* `cd OxfordAPI`
* `python OxfordDictionaries.py`


## Usage

The code below shows how to query APIv2 for definitions of word 'staple'.



```python
from oxforddictionaries.caching_language_dictionary import CachingLanguageDictionary
from oxforddictionaries.credentials import APPLICATION_ID, APPLICATION_KEY
from oxforddictionaries.oxford_api_v2 import OxfordApiV2

if __name__ == "__main__":
    oxford_api = OxfordApiV2(APPLICATION_ID, APPLICATION_KEY)
    caching_language_dictionary = CachingLanguageDictionary(oxford_api, 'en-gb')
    result = caching_language_dictionary.get_definitions("staple")
    print(result)
```
Note: before using it you need to create python file credentials.py in oxforddictionaries directory of the following structure:
```python
# this file is part of git ignore, replace with your API credentials
APPLICATION_ID = ""
APPLICATION_KEY = ""
```
## Contributing

1. Fork it! :+1:
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :+1:
