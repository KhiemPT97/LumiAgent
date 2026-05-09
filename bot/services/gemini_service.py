import google.generativeai as genai
from bot.config import config

class GeminiService:
    def __init__(self):
        genai.configure(api_key=config.GEMINI_API_KEY)
        # Use gemini-flash-latest which is available in your account
        self.model = genai.GenerativeModel(
            model_name='gemini-flash-latest',
            system_instruction=(
                "Vai trò: Bạn là 'Lumi', một chuyên gia lập trình toàn năng (Full-stack Developer).\n"
                "Mục tiêu: Hỗ trợ xây dựng, tối ưu hóa ứng dụng và xử lý lỗi từ Frontend đến Backend.\n"
                "Phong cách: Chuyên nghiệp, nhạy bén, súc tích, ngôn ngữ Senior Developer.\n"
                "Hành vi: \n"
                "- Luôn hỏi về ngôn ngữ/nền tảng đang làm việc.\n"
                "- Trình bày code sạch trong khối mã.\n"
                "- Chỉ ra lỗi và đề xuất phương án khắc phục lịch sự."
            )
        )
        self.chat = self.model.start_chat(history=[])

    async def generate_response(self, prompt: str) -> str:
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            return f"Error connecting to Gemini: {str(e)}"

gemini_service = GeminiService()
