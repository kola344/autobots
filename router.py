from aiogram import Router, F
from aiogram.types import Message
from bots import connecting

router = Router()

@router.message(F.startswith('/connect'))
async def process_message(message: Message):
    token = message.text.split()[1]
    await connecting(token, router)
    await message.answer("Создание бота завершено")

@router.message(F.text)
async def process_messageeee(message: Message):
    await message.answer(message.text)