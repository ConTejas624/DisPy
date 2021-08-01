import asyncio
import enum
import aiohttp
import sys
from resources import __version__

class HTTP(enum.Enum):
    GET = "GET"
    POS = "POST"
    PUT = "PUT"
    PTC = "PATCH"
    DEL = "DELETE"

class Routes(enum.Enum):
    BASE = 'https://discord.com/api'
    VERSION = '/v9'

class API:
    def __init__(self, token) -> None:

        self.headers = {
            'User-Agent': 'DiscordBot (https://github.com/ConTejas624/DisPy {0}) Python/{1[0]}.{1[1]} aiohttp/{2}'.format(
                __version__, sys.version_info, aiohttp.__version__),
            'Authorization': 'Bot ' + token,
            'Content-Type': 'application/json'
        }

    async def __request(self, extension, payload=None) -> dict:
        url = Routes.BASE + Routes.VERSION + extension
        async with aiohttp.ClientSession() as session:
            if not payload == None:
                async with session.get(url, headers=self.headers, payload=payload) as response:
                    return await response.json()
            else:
                async with session.get(url, headers=self.headers) as response:
                    return await response.json()
    
    async def __post(self, extension, )