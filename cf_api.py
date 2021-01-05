from abc import ABC, abstractmethod
import json
import aiohttp
import asyncio
REQ_PREFIX = 'https://codeforces.com/api/'


# Inherit this class to any new method that is added.
# See 'commands.py' for examples
class Method(ABC):
    """
    An Abstract class which represents method of the cf-api.
    Refer: "https://codeforces.com/apiHelp/methods" for details of possbile methods.
    """
    @abstractmethod
    async def name(self) -> str:
        """
        Return the name of the method.
        """
        pass

    @abstractmethod
    async def params(self) -> str:
        """
        Return all the params in the request url for the cf-api.
        """
        pass

    async def get(self):
        """
        Performs the GET request and return the Json result
        """
        name = await self.name()
        params = await self.params()

        # Ideally should not make a new session for each request. 
        # Todo: Somehow re-use session.
        request = f'{REQ_PREFIX}{name}?{params}'
        async with aiohttp.ClientSession() as session:
            async with session.get(request) as response:
                return await response.json()
                # pass


