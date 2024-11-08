from aiogram import Bot, Dispatcher
from router import router

bots = {"7852532479:AAHu3tlY4ogxsz0gsd1b6kN6CS3CCd2_7Zs": {}}

async def connect_bot(token):
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    bots[token] = {"dp": dp, "bot": bot}
    await bot.set_webhook(url=f"https://svetlana-backend.onrender.com/webhook?bot_token={token}")
