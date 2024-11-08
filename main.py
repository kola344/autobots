from fastapi import FastAPI, Request
from typing import Any

import config
from router import router
from aiogram import Bot, Dispatcher
import bots
from aiogram.types import Update

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/webhook')
async def webhook(update: dict[str, Any], request: Request):
    bot_token = request.query_params.get('bot_token')
    dp = bots.bots[bot_token]["dp"]
    bot = bots.bots[bot_token]["bot"]
    await dp.feed_webhook_update(bot=bot, update=Update(**update))
    return {'status': 'ok'}

@app.on_event('startup')
async def on_startup():
    bot = Bot(token=config.test_token)
    dp = Dispatcher()
    bots.bots[config.test_token] = {"dp": dp, "bot": bot}
    dp.include_router(router)
    await bot.delete_webhook()
    await bot.set_webhook('https://svetlana-backend.onrender.com/webhook?bot_token=' + config.test_token, drop_pending_updates=True)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)