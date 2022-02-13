from config import settings, get_logger
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
from .loader import tg_client, tg_bot

logger = get_logger(__name__)


async def listen_channels(event: events.NewMessage):
    """
    Если какие-то из целевых слов есть в тексте и какое-то из 3х слов еще есть в сообщении - пересылаем в основной канал
    если из 3х слов нет ни одного - отправляем в резервный канал.
    помечаем сообщение, как прочитанное.
    :param event:
    :return:
    """

    if any(word in event.message.message.lower() for word in settings.FINDING_WORDS):
        logger.info(event)
        if any(trigger in event.message.message.lower() for trigger in ['ищу', 'вакансия', 'требуется']):
            await tg_client.forward_messages(settings.MAIN_CHANNEL_LINK, event.message.id, event.message.to_id)
            await tg_bot.send_message(settings.MAIN_CHANNEL_LINK, 'New announce')
        else:
            await tg_client.forward_messages(settings.RESERVED_CHANNEL_LINK, event.message.id, event.message.to_id)
            await tg_bot.send_message(settings.RESERVED_CHANNEL_LINK, 'New announce')
    else:
        logger.info("Useless!!")
    await event.message.mark_read()


# @tg_client.on(event=events.NewMessage())
async def test_h(event: events.NewMessage):
    logger.info(event.message)


