from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, ContextTypes, CallbackContext, CommandHandler, MessageHandler, CallbackQueryHandler, filters
#from telegram.error import TelegramError, NetworkError

BOT_API = "7226017383:AAHbvfq8nkcK3_2TtGJ98xmke_HMNLccmkU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.message.chat
    user = update.effective_user
    user = update.message.from_user
    username = user.username

    markup = ReplyKeyboardMarkup([["Text 1", "Text 2"], ["Text 3", "Text 4"]])

    await update.message.reply_text(f"Hello {username} Welcome to appclick July Bot from Telegram", reply_markup=markup)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    message = update.message.text
    markup = ReplyKeyboardRemove()

    match(message.lower()):
        case "text 1":
            await update.message.reply_text(text="You entered Text One", reply_markup=markup)
        case "text 2":
            await update.message.reply_text(text="You entered Text Two", reply_markup=markup)
        case "text 3":
            await update.message.reply_text(text="You entered Text Three", reply_markup=markup)
        case "text 4":
            await update.message.reply_text(text="You entered Text Four", reply_markup=markup)

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardRemove()

async def jumia(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    keyboard_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="View Jumia",url="https://jumia.com.ng")],[InlineKeyboardButton("Search Products", callback_data="search-product"), InlineKeyboardButton("Post Product", callback_data="post-product")]])
    await update.message.reply_text(text="Jumia Update Loaded", reply_markup=keyboard_markup)

async def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer(text="Loading")

    match(query.data) :
        case "search-product":
            await query.edit_message_text(text="Searching Products from Jumia")

        case "post-product" :
            await query.edit_message_text(text="Posting Products to Jumia")

def main():
    application = Application.builder().token(BOT_API).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("jumia", jumia))
    application.add_handler(CallbackQueryHandler( queryHandler))
    application.add_handler(MessageHandler( filters.TEXT & ~filters.COMMAND, message))
    print("Application Started")
    application.run_polling()


if __name__ == "__main__" :
    main()


