import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Environment Variables
BOT_TOKEN = os.getenv("7780706515:AAE6AnXIEPWySNHY7YOscfihm__Cv7EkgrM")
GEMINI_API_KEY = os.getenv("AIzaSyDqg7yYoU-UCwtlR2dqXP1b3GBy3DuQNXg")

# Set Gemini API Key
genai.configure(api_key=GEMINI_API_KEY)

# AI Response Function
def ai_response(text):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return "❌ AI response failed."

# Start Command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("👋 Welcome to AI WebDev Bot!\nAsk me anything about web development!")

# Handle Messages (AI-Generated Responses)
def handle_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    ai_reply = ai_response(user_text)
    update.message.reply_text(ai_reply)

# Main Function
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
