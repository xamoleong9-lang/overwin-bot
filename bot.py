from telegram.ext import Updater, CommandHandler

TOKEN = "8413553192:AAHPpz4yyTIP2gKVslqOKzlx2kUYYCMO1q4"

def start(update, context):
    update.message.reply_text(
        "⚽ OverWin Live Bot ενεργό!\n\n"
        "Κατάσταση: ΣΥΝΔΕΘΗΚΕ ✔️"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
