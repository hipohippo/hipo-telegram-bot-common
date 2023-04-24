from typing import List, Tuple, Optional

from telegram.ext import BaseHandler, Application, ApplicationBuilder
from telegram.ext._utils.types import JobCallback, CCT

from hipo_telegram_bot_common.bot_config import BotConfig


def bot_factory(
    bot_token: str,
    bot_config: BotConfig,
    handlers: Optional[List[BaseHandler]],
    repeating_jobs: Optional[List[Tuple[JobCallback[CCT], dict]]],
    onetime_jobs: Optional[List[Tuple[JobCallback[CCT], dict]]],
) -> Application:
    application = (
        ApplicationBuilder()
        .token(bot_token)
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .concurrent_updates(3)
        .build()
    )
    application.bot_data["bot_config"] = bot_config
    if handlers:
        application.add_handlers(handlers)

    if repeating_jobs:
        for repeating_job in repeating_jobs:
            application.job_queue.run_repeating(repeating_job[0], **repeating_job[1])

    if onetime_jobs:
        for onetime_job in onetime_jobs:
            application.job_queue.run_once(onetime_job[0], **onetime_job[1])
    return application
