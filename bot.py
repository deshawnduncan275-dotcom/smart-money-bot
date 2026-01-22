from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Welcome to Smart Money Alerts\n\n"
        "You’ll receive legit money-making opportunities.\n\n"
        "🆓 /free — Sample alerts\n"
        "⭐ /premium — Unlock premium alerts"
    )

async def free(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆓 FREE ALERT SAMPLE:\n\n"
        "Some apps pay $10–$30 for signups.\n"
        "Premium users get exact links + timing."
    )

async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⭐ PREMIUM ACCESS\n\n"
        "• Instant alerts\n"
        "• Full breakdowns\n"
        "• Exclusive opportunities\n\n"
        "Cost: ⭐️ 50 Stars / month\n\n"
        "Payment activation coming next 💳"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("free", free))
app.add_handler(CommandHandler("premium", premium))

app.run_polling()
