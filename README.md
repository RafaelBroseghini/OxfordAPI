# Oxford Dictionary API Python Wrapper

This is a python wrapper around the Oxford Dictionary API.
The Oxford API offers a free plan with up to 3,000 requests per month with full access to Oxford Dictionaries data, although you will need to register for an API key. Sign up [here](https://developer.oxforddictionaries.com/).

## Installation

* `git clone git@github.com:RafaelBroseghini/OxfordAPI.git`
* `cd OxfordAPI`
* `python OxfordDictionaries.py`


## Usage

The code below shows how to quickly get 10 synonyms for a chosen word.

```python
from oxforddictionaries.words import OxfordDictionaries

o = OxfordDictionaries(app_id, app_key)

relax = o.get_synonyms("absorb").json()

synonyms = relax['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']

for s in range(10):
    print(synonyms[s]['text'])

```
## Contributing

1. Fork it! :+1:
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :+1:
