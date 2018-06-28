# Oxford Dictionary API Python Wrapper

This is a python wrapper for the Oxford Dictionary API.
The Oxford API offers a free plan with up to 2,000 requests per month, although you will need an API key. Sign up [here](https://developer.oxforddictionaries.com/).

# Installation
`pass`

# Usage
```python
o = Oxford(app_id, app_key)

#print(o.get_info_about_word("book"))
relax = o.get_synonyms("absorb").json()

synonyms = relax['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']

for s in range(10):
    print(synonyms[s]['text'])```
