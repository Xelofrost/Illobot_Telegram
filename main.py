from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY= os.getenv("API_KEY")
async def saludo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: await update.message.reply_text("¡Hola!")
async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
    domain = context.args[0]
    resultados = subprocess.run(["./scan.sh", domain], capture_output=True, text=True, check=True)
    await update.message.reply_text(resultados.stdout)


def main():
    app = ApplicationBuilder().token(API_KEY).build()
    app.add_handler(CommandHandler("saludo", saludo))
    app.add_handler(CommandHandler("scan", scan))
    print("Bot activo")
    app.run_polling()

if __name__ =="__main__":
    main()