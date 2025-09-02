from telegram import Update#, InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery
from telegram.ext import Application, ContextTypes, CommandHandler#, MessageHandler, CallbackQueryHandler
#from telegram.error import TelegramError, NetworkError

BOT_API = "7226017383:AAHbvfq8nkcK3_2TtGJ98xmke_HMNLccmkU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.message.chat
    user = update.effective_user
    user = update.message.from_user
    username = user.username

    await update.message.reply_text(f"Hello {username} Welcome to appclick July Bot from Telegram")

def main():
    application = Application.builder().token(BOT_API).build()
    application.add_handler(CommandHandler("start", start))
    print("Application Started")
    application.run_polling()


if __name__ == "__main__" :
    main()


