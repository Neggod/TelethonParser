#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import os
import time
import logging
from configparser import ConfigParser, MissingSectionHeaderError

try:
    import socks
except (ImportError, ModuleNotFoundError):
    import sys
    import subprocess

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(BASE_DIR, 'requirements.txt')
    PIPE = subprocess.PIPE
    p = subprocess.Popen(sys.executable + f' -m pip3 install -r {input_file}', shell=True)
    p.wait()
    import socks
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='start_log.txt', level=logging.ERROR)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cfg = os.path.join(BASE_DIR, 'config.ini')

parser = ConfigParser()
try:
    parser.read(cfg, encoding='UTF-8')
except MissingSectionHeaderError:
    print('Someone edit config file with fucking windows notepad!')
    temp = None
    with open(cfg, 'rb') as config:
        temp = config.read().decode("utf-8-sig").encode("utf-8")
    with open(cfg, 'wb') as config:
        config.write(temp)
    parser.read(cfg, encoding='UTF-8')

# bot values
api_id = parser.get('App_values', 'api_id')
api_hash = parser.get('App_values', 'api_hash')

# target words
target_words = []
for word in parser['Target_Words'].values():
    target_words.append(word)

# init my channels
main_channel = parser.get('Project_Channels', 'MainChannel')
reserved_channel = parser.get('Project_Channels', 'ReservedChannel')

client = TelegramClient('work_session', api_id, api_hash, device_model='Tesla Model S',
                        # connection=connection.ConnectionTcpMTProxyIntermediate,
                        # если есть MTProto proxy - убрать решетки над и под этой надписью, отредактировать запись снизу
                        # главное скобки не упустить.
                        # proxy=('host', 443, 'secret'))
                        proxy=(socks.SOCKS5, '127.0.0.1', 1088))


async def listen_channels(event: events.NewMessage):
    """
    Если какие-то из целевых слов есть в тексте и какое-то из 3х слов еще есть в сообщении - пересылаем в основной канал
    если из 3х слов нет ни одного - отправляем в резервный канал.
    помечаем сообщение, как прочитанное.
    :param event:
    :return:
    """
    if any(word in event.message.message.lower() for word in target_words):
        if any(trigger in event.message.message.lower() for trigger in ['ищу', 'вакансия', 'требуется']):
            await client.forward_messages(main_channel, event.message.id, event.message.to_id)
        else:
            await client.forward_messages(reserved_channel, event.message.id, event.message.to_id)
    await event.message.mark_read()


async def prepare_donors(client_: TelegramClient):
    """
    Все группы доноры преобразуем в ID-ы, чтобы, если поменялась ссылка, не перестало работать.
    :return:
    """
    donors = []
    for number, query in parser['Donor_Channels'].items():
        if query.isdigit():
            donor: PeerChannel = PeerChannel(int(query))
        else:
            try:
                donor: PeerChannel = await client_.get_entity(query)
            except Exception as err:
                print(err)
                continue
            else:
                parser.set('Donor_Channels', number, str(donor.id))
        donors.append(donor)
    with open(cfg, 'w', encoding='UTF-8') as conf:
        parser.write(conf)
    print('Все ссылки успешно преобразованы.')
    client_.add_event_handler(listen_channels, events.NewMessage(chats=(*donors,)))


if __name__ == '__main__':
    client.start()
    client.loop.create_task(prepare_donors(client))
    client.run_until_disconnected()
