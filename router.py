from aiogram import Router, F
from aiogram.types import Message
from bots import connecting

router = Router()

@router.message(F.text)
async def process_messageeee(message: Message):
    if '/connect' in message.text:
        token = message.text.split()[1]
        await connecting(token)
        await message.answer("Создание бота завершено")
    await message.answer(message.text)