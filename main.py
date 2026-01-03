import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher

from app.getprice import get_ton_price
from config import Config_Obj

logging.basicConfig(level=logging.INFO)


async def post_ton_price(bot: Bot):
    while True:
        try:
            usd, rub = await get_ton_price()

            await bot.send_message(
                chat_id=Config_Obj.channel_id,

                text=f"{usd} $\n{rub} ₽",

                parse_mode="Markdown"
            )

        except Exception as e:
            logging.error(f"Ошибка получения цены TON: {e}")

        await asyncio.sleep(Config_Obj.post_interval)


async def main():
    bot = Bot(token=Config_Obj.bot_token)

    dp = Dispatcher()

    asyncio.create_task(post_ton_price(bot))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
