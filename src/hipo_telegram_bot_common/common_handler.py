import pandas as pd
from telegram import Update, BotCommand
from telegram.ext import ContextTypes

from hipo_telegram_bot_common.bot_config.bot_config import BotConfig


# handlers will be applied in the order defined...if accepted by one handler, it will stop processing more rules
# https://stackoverflow.com/questions/77034884/how-to-make-my-telegram-bots-handler-not-block-each-other


async def heart_beat_job(context: ContextTypes.DEFAULT_TYPE):
    bot_config: BotConfig = context.bot_data["bot_config"]
    active = pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M")
    bot_config.redis_conn.hmset(bot_config.bot_name, {"last_active": active})

    await context.bot.send_message(
        chat_id=bot_config.heart_beat_chat,
        text=f"heart beat from {bot_config.bot_name} at {active} UTC",
    )


async def poke_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message.text.split(" ")[0] == "/poke"
    await update.message.reply_text("poke back")


async def error_notification_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ## TODO
    bot_config: BotConfig = context.bot_data["bot_config"]
    await context.bot.send_message(chat_id=bot_config.error_notify_chat)


async def init_commands_job(context: ContextTypes.DEFAULT_TYPE):
    ## TODO
    commands = [
        BotCommand("/bedroom_on", "turn on bedroom"),
        BotCommand("/bedroom_off", "turn off bedroom"),
    ]
    await context.bot.setMyCommands(commands)
    # await context.bot.deleteMyCommands()
