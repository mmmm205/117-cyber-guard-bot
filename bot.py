from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import re
import os

TOKEN = "8412332912:AAGSLj9Bope71NrLOAccAiP31je6yaMq5Ak"

def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=\-]", password):
        score += 1

    if score <= 2:
        return "❌ ضعيفة"
    elif score <= 4:
        return "⚠️ متوسطة"
    else:
        return "✅ قوية"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ Cyber Guard Bot\n\n"
        "بوت فحص أمني يساعدك على:\n"
        "🔐 فحص كلمات المرور\n"
        "🌐 اكتشاف الروابط المشبوهة\n"
        "🌍 تحليل عناوين IP\n\n"
        "━━━━━━━━━━━━━━\n"
        "👨‍💻 Developed by: Eng. Majid Alnaqbi\n"
        "━━━━━━━━━━━━━━\n\n"
        "الأوامر:\n"
        "/password <كلمة المرور>\n"
        "/url <الرابط>\n"
        "/ip <عنوان IP>"
    )

async def check_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ اكتب كلمة المرور بعد الأمر")
        return
    pwd = context.args[0]
    await update.message.reply_text(f"🔐 نتيجة الفحص: {password_strength(pwd)}")

async def check_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ اكتب الرابط بعد الأمر")
        return
    url = context.args[0]
    if url.startswith("http://"):
        await update.message.reply_text("⚠️ الرابط غير آمن (HTTP)")
    else:
        await update.message.reply_text("✅ الرابط يبدو آمن مبدئيًا")

async def check_ip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ اكتب عنوان IP")
        return
    ip = context.args[0]
    if ip.startswith(("192.", "10.", "172.")):
        await update.message.reply_text("ℹ️ IP خاص (Private Network)")
    else:
        await update.message.reply_text("🌍 IP عام – يُفضل فحصه بأدوات متقدمة")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("password", check_password))
    app.add_handler(CommandHandler("url", check_url))
    app.add_handler(CommandHandler("ip", check_ip))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
