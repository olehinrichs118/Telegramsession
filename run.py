from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from decouple import config

APP_ID = config("APP_ID", default=0, cast=int)
API_HASH = config("API_HASH", default=None, cast=str)

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
