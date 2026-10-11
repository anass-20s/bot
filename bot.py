from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = '8910663013:AAEMbJAiDjFfNuUWVGETFVqY-ajNHaGr6Lc'

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_member in update.message.new_chat_members:
        if new_member.id == context.bot.id:
            continue
        first_name = new_member.first_name
        welcome_text = f"مرحبا بك {first_name} في فريق Aurex نتمنى لك التوفيق والنجاح"
        await update.message.reply_text(welcome_text)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    print("البوت يعمل الآن ومستعد للترحيب بالأعضاء...")
    application.run_polling()

if __name__ == '__main__':
    main()
