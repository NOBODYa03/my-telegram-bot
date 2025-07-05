from telegram import Update, ChatMember
from telegram.ext import ApplicationBuilder, MessageHandler, ChatMemberHandler, filters, ContextTypes

def load_bad_words():
    with open("badwords.txt", "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

BAD_WORDS = load_bad_words()

async def check_bad_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    text = update.message.text.lower()
    if any(bad_word in text for bad_word in BAD_WORDS):
        await context.bot.send_message(
            chat_id=update.message.chat_id,
            text="⚠️iltimos sokinmang undan kora odobli qiz 🧕🏻 va bola 👳🏻 boling✅"
        )

        try:
            await update.message.delete()
        except:
            pass

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men Sokmang botman! Endi log yozmayman, faqat ogohlantiraman.")

async def bot_added(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.my_chat_member.chat
    old_status = update.my_chat_member.old_chat_member.status
    new_status = update.my_chat_member.new_chat_member.status

    if old_status in ["left", "kicked"] and new_status == "member":
        text = (
            "Salom guruh a'zolari! 👋\n\n"
            "✅ Menga quyidagi huquqlar kerak:\n"
            "• Xabarlarni o'qish\n"
            "• Xabarlarni o‘chirish\n\n"
            "⚠️ Shunda men yomon so'zlarni o‘chira olaman va guruhni pok saqlayman!"
        )
        try:
            await context.bot.send_message(chat_id=chat.id, text=text)
        except Exception as e:
            print(f"Xabar yuborishda xato: {e}")

def main():
    TOKEN = "8181225282:AAGRrAtiIX_x2u6JofDlfccWKoXlBilqpI0"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.COMMAND & filters.Regex('^/start$'), start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_bad_words))
    app.add_handler(ChatMemberHandler(bot_added, ChatMemberHandler.MY_CHAT_MEMBER))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
