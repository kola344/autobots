from router import router
from aiogram import Bot, Dispatcher

async def connect_bot(token):
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await bot.set_webhook(url=f"https://svetlana-backend.onrender.com/webhook?bot_token={token}")
    return dp, bot