import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def surebet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    odds = list(map(float, context.args))
    if len(odds) != 3:
        await update.message.reply_text("Kullanım:\n/surebet 2.10 3.60 4.40")
        return

    o1, ox, o2 = odds
    total = (1/o1) + (1/ox) + (1/o2)
    msg = "✅ SUREBET VAR" if total < 1 else "❌ SUREBET YOK"
    await update.message.reply_text(f"{msg}\nToplam: {total:.3f}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("surebet", surebet))
    print("Bot çalışıyor...")
    app.run_polling()

def run_fake_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), BaseHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_fake_server).start()

if __name__ == "__main__":
    main()
