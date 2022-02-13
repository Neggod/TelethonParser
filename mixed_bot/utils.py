from config import settings, get_logger
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
from .handlers import listen_channels

logger = get_logger(__name__)

logger.info("Listening channels/groups/bots:\n{0}".format('\n'.join(settings.TARGETS)))


async def prepare_donors(client: TelegramClient):
    """
    Все группы доноры преобразуем в ID-ы, чтобы, если поменялась ссылка, не перестало работать.
    :return:
    """
    donors = []
    for query in settings.TARGETS:
        try:
            donor: PeerChannel = await client.get_entity(query)
        except Exception as err:
            logger.error(err)
        else:
            donors.append(donor)
    logger.info(f"Donors is {donors}")
    client.add_event_handler(listen_channels, events.NewMessage(chats=(*donors,)))
    return client
