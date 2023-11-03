import logging
import sys

from telegram.ext import CommandHandler, Application

from hipo_telegram_bot_common.bot_config.bot_config_parser import parse_from_ini
from hipo_telegram_bot_common.bot_factory import BotBuilder
from hipo_telegram_bot_common.common_handler import heart_beat_job
from hipo_telegram_bot_common.daemon.bot_daemon_config import BotDaemonConfig
from hipo_telegram_bot_common.daemon.handler import start_bot_handler, stop_bot_handler


def build_bot_app(bot_config_dict) -> Application:
    bot_config = BotDaemonConfig(bot_config_dict)
    bot_app = (
        BotBuilder(bot_config_dict["bot_token"], bot_config)
        .add_handlers([CommandHandler("start", start_bot_handler), CommandHandler("stop", stop_bot_handler),])
        .add_repeating_jobs([(heart_beat_job, {"first": 5, "interval": 3600})])
        .build()
    )
    return bot_app


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    bot_config_file = sys.argv[1]
    bot_config_dict = parse_from_ini(bot_config_file)
    bot_app = build_bot_app(bot_config_dict)
    bot_app.run_polling()
