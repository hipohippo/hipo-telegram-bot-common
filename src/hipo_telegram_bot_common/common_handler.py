import pandas as pd
from telegram.ext import ContextTypes

from hipo_telegram_bot_common.bot_config import BotConfig


async def heart_beat_job(context: ContextTypes.DEFAULT_TYPE):
    bot_config: BotConfig = context.bot_data["bot_config"]
    await context.bot.send_message(
        chat_id=bot_config.heart_beat_chat,
        text=f"heart beat from {bot_config.bot_name} at {pd.Timestamp.utcnow().strftime('%Y-%m-%d %H:%M')} UTC",
    )


async def error_notification_handler(update, context):
    bot_config: BotConfig = context.bot_data["bot_config"]
    await context.bot.send_message(chat_id=bot_config.error_notify_chat)
