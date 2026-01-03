import aiohttp

from config import Config_Obj

async def get_ton_price():
    """
    Получает цену TON, используя aiohttp
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(Config_Obj.ton_api_url) as resp:

            data = await resp.json()
            ton = data["the-open-network"]

            return ton["usd"], ton["rub"]
