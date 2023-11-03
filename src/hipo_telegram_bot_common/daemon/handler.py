import subprocess

from telegram import Update
from telegram.ext import ContextTypes

from hipo_telegram_bot_common.util import restricted


@restricted
async def start_bot_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_name = update.message.text.split(" ")[1]
    bot_exec = {"mta": "/home/hipo/botrun/bot/mta-subway-bot/start-mta-subway-bot.sh"}
    bot_log = {"mta": "/home/hipo/botrun/bot/mta-subway-bot/mta-subway-bot.log"}

    p = subprocess.Popen(bot_exec[bot_name], stdout=bot_log[bot_name], start_new_session=True)
    await update.message.reply_text(text=f"{p.pid}: started {bot_exec}", parse_mode="HTML")


@restricted
async def stop_bot_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.split(" ")
    pid = msg[1]
    subprocess.run(["kill", "-9", str(pid)])
    await update.message.reply_text(text=f"{pid}: stopped", parse_mode="HTML")
