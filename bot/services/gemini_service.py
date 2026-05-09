import os
import google.generativeai as genai
from bot.config import config

class GeminiService:
    def __init__(self):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name='gemini-flash-latest',
            system_instruction=(
                "Vai trò: Bạn là 'Lumi', một chuyên gia lập trình toàn năng (Full-stack Developer).\n"
                "Mục tiêu: Hỗ trợ xây dựng, tối ưu hóa ứng dụng và xử lý lỗi từ Frontend đến Backend.\n"
                "Phong cách: Chuyên nghiệp, nhạy bén, súc tích, ngôn ngữ Senior Developer.\n"
                "Kỹ năng đặc biệt: Bạn có quyền truy cập vào bộ kỹ năng 'agent-skills' để thực hiện các quy trình kỹ thuật chuẩn chỉnh. "
                "Khi người dùng yêu cầu lập kế hoạch, viết tài liệu, build code hoặc review, hãy tham chiếu đến các workflow tương ứng trong thư mục agent-skills/skills/."
            )
        )
        self.chat = self.model.start_chat(history=[])

    def get_skill_content(self, skill_folder: str) -> str:
        """Đọc nội dung file SKILL.md từ thư mục kỹ năng tương ứng."""
        skill_path = os.path.join("agent-skills", "skills", skill_folder, "SKILL.md")
        if os.path.exists(skill_path):
            with open(skill_path, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    async def generate_response(self, prompt: str, skill_folder: str = None) -> str:
        try:
            full_prompt = prompt
            if skill_folder:
                skill_content = self.get_skill_content(skill_folder)
                if skill_content:
                    full_prompt = f"Sử dụng quy trình kỹ năng sau đây để thực hiện yêu cầu:\n\n{skill_content}\n\nUser Request: {prompt}"
            
            response = await self.model.generate_content_async(full_prompt)
            return response.text
        except Exception as e:
            return f"Error connecting to Gemini: {str(e)}"

gemini_service = GeminiService()
