import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция на /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "Привет! Вот две полезные ссылки:\n\n"
        "[Перейти на Google](https://google.com)\n"
        "[Перейти на YouTube](https://youtube.com)"
    )
    await update.message.reply_text(message, parse_mode="Markdown")

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token("7959795652:AAHPijRlzY9UjoUTLLGLBCgw0xhIXytxbn4").build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен! Ожидаем команды /start в Telegram...")  # Важно!
    app.run_polling()
