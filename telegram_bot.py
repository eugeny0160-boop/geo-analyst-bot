from telegram import Bot
from config import TELEGRAM_BOT_TOKEN

async def send_summary_to_channel(summary_text: str, channel_id: str):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=channel_id, text=summary_text, parse_mode="Markdown")