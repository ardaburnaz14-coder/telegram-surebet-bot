from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8295376924:AAGVugtZpaa9lpBtueptv2K9DV18x3Bd1Zg"

async def surebet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        odds = list(map(float, context.args))
        if len(odds) != 3:
            await update.message.reply_text(
                "Kullanım:\n/surebet 2.10 3.60 4.40"
            )
            return

        o1, ox, o2 = odds
        total = (1 / o1) + (1 / ox) + (1 / o2)

        if total < 1:
            msg = f"✅  SUREBET VAR\nToplam: {total:.3f}"
        else:
            msg = f"❌  SUREBET YOK\nToplam: {total:.3f}"

        await update.message.reply_text(msg)

    except Exception:
        await update.message.reply_text(
            "Hata! Doğru format:\n/surebet 2.10 3.60 4.40"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("surebet", surebet))

    print("Bot çalışıyor... Telegram'dan /surebet ile test edebilirsiniz.")
    app.run_polling()

if __name__ == "__main__":
    main()
