import asyncio
import aiohttp
import sys


__version__ = 'test build'
__base_url__ = 'https://discord.com/api/v9'


class HTTPClient:
    def __init__(self, token) -> None:

        self.headers = {
            'User-Agent': 'DiscordBot (https://github.com/ConTejas624/DisPy {0}) Python/{1[0]}.{1[1]} aiohttp/{2}'.format(
                __version__, sys.version_info, aiohttp.__version__),
            'Authorization': 'Bot ' + token
        }

    async def get(self, session: aiohttp.ClientSession, extension: str, data=None) -> dict:
        url = __base_url__ + extension
        if not data == None:
            async with session.get(url, headers=self.headers, data=data) as response:
                return await response.json()
        else:
            async with session.get(url, headers=self.headers) as response:
                return await response.json()
    
    async def post(self, session: aiohttp.ClientSession, extension, data):
        url = __base_url__ + extension
        async with session.post(url, headers=self.headers, data=data) as response:
            return await response.json()
    
    async def delete(self, session: aiohttp.ClientSession, extension, data=None):
        url = __base_url__ + extension
        if not data == None:
            async with session.delete(url, headers=self.headers, data=data) as response:
                return await response.json()
        else:
            async with session.delete(url, headers=self.headers) as response:
                return await response.json()
    
    async def patch(self, session: aiohttp.ClientSession, extension, data):
        url = __base_url__ + extension
        async with session.patch(url, headers=self.headers, data=data) as response:
            return await response.json()