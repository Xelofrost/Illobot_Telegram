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
async def nmap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) < 1:
        await update.message.reply_text("Por favor, proporciona un dominio o IP para escanear.")
        return

    domain = context.args[0]
    try:
        # Ejecutar nmap en el dominio proporcionado
        resultados = subprocess.run(
            ["nmap", domain], capture_output=True, text=True, check=True
        )
        # Responder con el resultado del escaneo
        await update.message.reply_text(resultados.stdout)
    except subprocess.CalledProcessError as e:
        # En caso de error con el comando nmap
        await update.message.reply_text(f"Error al ejecutar nmap: {e.stderr}")


def main():
    app = ApplicationBuilder().token(API_KEY).build()
    app.add_handler(CommandHandler("saludo", saludo))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("nmap", nmap))  # Comando /nmap
    print("Bot activo")
    app.run_polling()

if __name__ =="__main__":
    main()