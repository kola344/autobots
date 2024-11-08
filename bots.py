from aiogram import Bot, Dispatcher
from connect_bot import connect_bot

bots = {"7852532479:AAHu3tlY4ogxsz0gsd1b6kN6CS3CCd2_7Zs": {}}

async def connecting(token, router):
    dp, bot = connect_bot(token, router)
    bots[token] = {"dp": dp, "bot": bot}
    await bot.set_webhook(url=f"https://svetlana-backend.onrender.com/webhook?bot_token={token}")
