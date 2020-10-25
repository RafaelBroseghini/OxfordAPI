from oxford_api import OxfordApi


class OxfordDictionaries:
    def __init__(
            self,
            oxford_api: OxfordApi,
            language='en'):
        self.oxford_api = oxford_api
        self.lang = language

