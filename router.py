from aiogram import Router, F
from aiogram.types import Message
from bots import connecting

router = Router()

@router.message(F.text == '/create')
async def process_message(message: Message):
    await message.answer("Введите токен")
    await connecting(message.text)
    await message.answer("Создание бота завершено")

@router.message(F.text)
async def process_messageeee(message: Message):
    await message.answer(message.text)