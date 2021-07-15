import asyncio
import enum
import aiohttp

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
        pass

    async def __request(self, extension, payload) -> dict:
        url = Routes.BASE + Routes.VERSION + extension
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                pass