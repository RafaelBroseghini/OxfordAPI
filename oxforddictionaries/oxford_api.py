from abc import ABC, abstractmethod


class OxfordApi(ABC):
    @abstractmethod
    def send_request(self, lang, path, method='GET'):
        pass
