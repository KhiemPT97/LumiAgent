from aiogram import Router, types
from aiogram.filters import Command
from bot.services.gemini_service import gemini_service

router = Router()

# Danh sách mapping giữa lệnh Telegram và thư mục skill tương ứng
SKILL_MAP = {
    "spec": "spec-driven-development",
    "plan": "planning-and-task-breakdown",
    "build": "incremental-implementation",
    "test": "test-driven-development",
    "review": "code-review-and-quality",
    "ship": "shipping-and-launch",
    "simplify": "code-simplification",
    "debug": "debugging-and-error-recovery"
}

@router.message(Command("spec", "plan", "build", "test", "review", "ship", "simplify", "debug"))
async def handle_skill_commands(message: types.Message):
    # Lấy tên lệnh (bỏ dấu /)
    command = message.text.split()[0][1:].lower()
    
    # Lấy nội dung yêu cầu của người dùng sau lệnh
    user_request = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
    
    if not user_request:
        await message.reply(f"Vui lòng nhập yêu cầu của bạn sau lệnh /{command}. Ví dụ: `/{command} xây dựng tính năng đăng nhập`")
        return

    skill_folder = SKILL_MAP.get(command)
    
    loading_msg = await message.reply(f"🚀 Lumi đang thực hiện quy trình `{command}` chuyên sâu... Đợi một chút nhé!")
    
    # Gọi Gemini với Skill tương ứng
    response_text = await gemini_service.generate_response(user_request, skill_folder=skill_folder)
    
    await loading_msg.delete()
    await message.reply(response_text)

@router.message(Command("skills"))
async def list_skills(message: types.Message):
    skills_list = "\n".join([f"/{k}: {v.replace('-', ' ').title()}" for k, v in SKILL_MAP.items()])
    await message.reply(f"🎯 **Các kỹ năng chuyên gia của Lumi:**\n\n{skills_list}\n\nSử dụng lệnh kèm theo yêu cầu của bạn.")
