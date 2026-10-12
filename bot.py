import os
import html
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("متغير البيئة BOT_TOKEN غير موجود")

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_member in update.message.new_chat_members:
        if new_member.id == context.bot.id or new_member.is_bot:
            continue

        name = html.escape(new_member.first_name)
        mention = f'<a href="tg://user?id={new_member.id}">{name}</a>'
        welcome_text = f"مرحبا بك {mention} في فريق Aurex نتمنى لك التوفيق والنجاح"

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=welcome_text,
            parse_mode="HTML",
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"حدث خطأ: {context.error}")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member)
    )
    application.add_error_handler(error_handler)
    print("البوت يعمل الآن ومستعد للترحيب بالأعضاء...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
