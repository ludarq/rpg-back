from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = "7701212586:AAE9tAUbvIa8y6VvmbNjL7QV436tGGuUmv0"  # Замените на ваш токен

async def start(update: Update, context):
    # Отправляем приветственное сообщение с кнопкой для запуска WebApp
    await update.message.reply_text(
        "Добро пожаловать в RPG! Нажмите на кнопку ниже, чтобы начать.",
        reply_markup={"inline_keyboard": [[{
            "text": "Начать игру",
            "web_app": {"url": "https://rpgaidnd.vercel.app"}
        }]]}
    )

if __name__ == "__main__":
    # Запускаем приложение
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
