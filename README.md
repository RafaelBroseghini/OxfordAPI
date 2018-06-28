# Oxford Dictionary API Python Wrapper

This is a python wrapper for the Oxford Dictionary API.
The Oxford API offers a free plan with up to 2,000 requests per month, although you will need an API key. Sign up [here](https://developer.oxforddictionaries.com/).

# Installation
`pass`

# Usage
The code below shows how to quickly get 10 synonyms for a chosen word.
```python
from oxford import OxfordDictionaries
o = OxfordDictionaries.Oxford(app_id, app_key)

#print(o.get_info_about_word("book"))
relax = o.get_synonyms("absorb").json()

synonyms = relax['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']

for s in range(10):
    print(synonyms[s]['text'])
```

# Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :+1:
