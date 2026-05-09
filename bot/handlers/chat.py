from aiogram import Router, types, F
from bot.services.gemini_service import gemini_service

router = Router()

@router.message(F.text)
async def chat_handler(message: types.Message):
    # Check if we should respond in group
    if message.chat.type in ["group", "supergroup"]:
        bot_info = await message.bot.get_me()
        if not (f"@{bot_info.username}" in message.text or "Lumi ơi" in message.text):
            return

    # Show typing status
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    # Generate response from Gemini
    response = await gemini_service.generate_response(message.text)
    
    # Reply to user
    await message.reply(response)
