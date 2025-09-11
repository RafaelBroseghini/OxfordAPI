> [!CAUTION]
> This project has moved from [pip install oxforddictionaries](https://pypi.org/project/oxforddictionaries/) to [pip install oxfordapi](https://pypi.org/project/oxfordapi/)

# Oxford Dictionary API Python Wrapper

This project offers a simple client for the [Oxford Dictionary API](https://developer.oxforddictionaries.com/).

## Getting your App Key and ID

To get your App Key and ID, please follow the [Getting Started](https://developer.oxforddictionaries.com/documentation/getting_started) guide.

## Installation

`pip install oxfordapi`

## Usage

```python
from oxfordapi import Client

async def main():
  oxford_api = Client("<app_id>", "<app_key>")
  print(await oxford_api.get_entries("word"))

if __name__ == "__main__":
    asyncio.run(main())
```
