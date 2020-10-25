from abc import ABC, abstractmethod


class OxfordApi(ABC):
    @abstractmethod
    def send_request(self, path, method='GET'):
        pass

    @abstractmethod
    def get_entries(self, lang, word):
        pass
