from dotenv import load_dotenv
import os

load_dotenv()

class Config_Obj:
    bot_token = os.getenv("BOT_TOKEN")
    channel_id = os.getenv("CHANNEL_ID")

    post_interval = int(os.getenv("POST_INTERVAL"))

    ton_api_url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=the-open-network&vs_currencies=usd,rub"
    )