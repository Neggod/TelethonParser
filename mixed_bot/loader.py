from aiogram import Bot
from config import get_logger, settings

from telethon import TelegramClient

logger = get_logger(__name__)

tg_client = TelegramClient('client_session', api_id=settings.API_ID, api_hash=settings.API_HASH,
                           proxy=settings.PROXY)
logger.debug(f'Client {tg_client} is initialised')

tg_bot = TelegramClient('bot_session', api_id=settings.API_ID, api_hash=settings.API_HASH,
                        proxy=settings.PROXY)
# tg_bot.start(bot_token=settings.BOT_TOKEN)
