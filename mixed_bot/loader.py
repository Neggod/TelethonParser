import asyncio
from config import get_logger, settings

from telethon import TelegramClient
import socks
logger = get_logger(__name__)

tg_client = TelegramClient('client_session', api_id=settings.API_ID, api_hash=settings.API_HASH,
                           proxy=(socks.SOCKS5, '127.0.0.1', 1088))

tg_bot = TelegramClient('bot_session', api_id=settings.API_ID, api_hash=settings.API_HASH, proxy=(socks.SOCKS5, '127.0.0.1', 1088))
# tg_bot.start(bot_token=settings.BOT_TOKEN)