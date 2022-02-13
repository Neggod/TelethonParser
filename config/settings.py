from dotenv import load_dotenv
import os
from pathlib import Path
import socks

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
load_dotenv(BASE_DIR / '.env')

LOG_DIR = BASE_DIR / 'logs/'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# APP variables
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
# Useless in current variation
BOT_TOKEN = os.getenv("BOT_TOKEN", 'error')
# Redis auth values
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_USERNAME = os.getenv('REDIS_USERNAME', None)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_DB = int(os.getenv('REDIS_DB', 4))

# link for announces which 100% allowable
MAIN_CHANNEL_LINK = os.getenv('MAIN_CHANNEL', '')
# link for announces which have some key words
RESERVED_CHANNEL_LINK = os.getenv('RESERVED_CHANNEL')

# list of finding words
FINDING_WORDS = os.getenv('FINDING_WORDS').split(':')
# list of listening channels
TARGETS = os.getenv('TARGETS').split(';;')


DEBUG = True

PROXY = (socks.SOCKS5, '127.0.0.1', 1088) if DEBUG else None
