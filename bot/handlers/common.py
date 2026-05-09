from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Chào anh em! Tôi là Lumi 🤖\n"
        "Một chuyên gia Full-stack Developer. Anh em đang code dự án bằng ngôn ngữ hay nền tảng nào thế?"
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Các lệnh hỗ trợ:\n"
        "/start - Bắt đầu bot\n"
        "/help - Xem hướng dẫn sử dụng"
    )
