import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from bot.config import config
from bot.handlers import common, chat

async def main():
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout
    )

    # Initialize bot and dispatcher
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    from bot.handlers import common, chat, commands
    dp.include_router(common.router)
    dp.include_router(commands.router)
    dp.include_router(chat.router)

    # Start polling
    logging.info("Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
