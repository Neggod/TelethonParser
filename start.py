import asyncio
from config import get_logger, settings
from mixed_bot import tg_client, prepare_donors, tg_bot

logger = get_logger(__name__)
print(1)
if __name__ == '__main__':
    print(2)
    logger.info(f"Let's start")
    tg_client.start()
    tg_bot.start(bot_token=settings.BOT_TOKEN)
    loop = asyncio.get_event_loop()

    cl = tg_client.loop.create_task(prepare_donors(tg_client))
    logger.info(cl)

    tg_client.run_until_disconnected()
