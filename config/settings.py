from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
load_dotenv(BASE_DIR / '.env')

LOG_DIR = BASE_DIR / 'logs/'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# env variables
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv("BOT_TOKEN", 'error')
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_USERNAME = os.getenv('REDIS_USERNAME', None)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_DB = int(os.getenv('REDIS_DB', 4))
MAIN_CHANNEL_LINK = os.getenv('MAIN_CHANNEL', '')
RESERVED_CHANNEL_LINK = os.getenv('RESERVED_CHANNEL')

FINDING_WORDS = os.getenv('FINDING_WORDS').split(':')
TARGETS = os.getenv('TARGETS').split(':')