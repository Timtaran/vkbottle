from abc import ABC, abstractmethod
import typing


class ABCAPI(ABC):
    """ Abstract API class
    Documentation: https://github.com/timoniq/vkbottle/tree/v3.0/docs/api/api.md
    """

    @abstractmethod
    async def request(self, method: str, data: dict) -> dict:
        """ Makes a single request opening a session """
        pass

    @abstractmethod
    async def validate_response(self, response: dict) -> typing.Any:
        pass