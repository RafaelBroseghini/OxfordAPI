# Oxford Dictionary API Python Wrapper

This is a python wrapper around the [Oxford Dictionary API](https://developer.oxforddictionaries.com/).

## Getting your App Key and ID

To get your App Key and ID, please follow the [Getting Started](https://developer.oxforddictionaries.com/documentation/getting_started) guide.

## Installation

`pip install oxforddictionaries`

## Usage

```python
from oxforddictionaries import OxfordApi

async def main():
  oxford_api = OxfordApi("<app_id>", "<app_key>")
  print(await oxford_api.get_entries("word"))

if __name__ == "__main__":
    asyncio.run(main())
```

## Contributing

1. Fork it! :+1:
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :+1:
