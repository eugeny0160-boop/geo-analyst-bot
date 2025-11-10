# telegram_bot.py

import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ID первого бота (который отправляет статьи)
SOURCE_BOT_ID = 8325055385 # ← ЗАМЕНИ НА РЕАЛЬНЫЙ ID ПЕРВОГО БОТА!

# ID каналов, из которых читаем (вставь сюда правильные ID, начинающиеся с -100...)
CHANNEL_IDS = [2923537056, 2914190770]

async def handle_article(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    if not message or not message.from_user or not message.chat:
        return

    # Проверяем, что сообщение пришло из нужного канала
    if message.chat.id not in CHANNEL_IDS:
        return

    # Проверяем, что сообщение от нужного бота
    if message.from_user.id == SOURCE_BOT_ID:
        text = message.text or message.caption or ""
        if not text.strip():
            logger.info("Пустое сообщение от бота — пропускаем.")
            return

        logger.info(f"Получено сообщение от бота в канале {message.chat.title}: {text[:100]}...")

        try:
            # Импортируем анализатор
            from analyzer import analyze_article
            analysis_result = await analyze_article(text)

            # Сохраняем в базу
            from database import save_article_to_db
            await save_article_to_db(text, analysis_result)

            logger.info("✅ Статья успешно сохранена в базу.")

        except Exception as e:
            logger.error(f"Ошибка при обработке статьи: {e}")

def main():
    # Получаем токен из переменных окружения
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("Токен Telegram не найден в переменных окружения!")
        return

    # Создаём приложение
    app = Application.builder().token(token).build()

    # Добавляем обработчик сообщений
    app.add_handler(MessageHandler(filters.TEXT | filters.CAPTION, handle_article))

    logger.info("🚀 Бот запущен и слушает каналы...")
    app.run_polling()

if __name__ == '__main__':
    main()
