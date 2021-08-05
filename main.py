from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=1947866215:AAG_bqpQ-7vTj5dhoG9V_mQqGcThtvmEcXE,
    plugins=dict(root="handlers")
)

bot.start()
run()
