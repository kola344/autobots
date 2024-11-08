from aiogram import Dispatcher, Bot

dp = Dispatcher()

bots = {}

async def connecting(token):
    bot = Bot(token)
    bots[token] = bot
    await bot.delete_webhook()
    await bot.set_webhook(url=f"https://svetlana-backend.onrender.com/webhook?bot_token={token}")
