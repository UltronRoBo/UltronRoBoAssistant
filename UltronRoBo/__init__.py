"""
MIT License

Copyright (c) 2021 UltronRoBo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
import os
import sys
import time
import spamwatch

import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient
from telethon.sessions import StringSession

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.9, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 9:
    LOGGER.error(
        "You MUST have a python version of at least 3.9! Multiple features depend on this. Bot quitting..."
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    BOT_ID = int(os.environ.get("BOT_ID", None))
    DB_URI = os.environ.get("DATABASE_URL")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', True))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADBQADNwUAArR1kFY-CJ2yw8eczQI")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    GROUP_BOT_SESSION = os.environ.get("GROUP_BOT_SESSION", None)

    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

    
#-----------------------------------------------UltronRoBo/services/telethonuserbot.py (ENV)-------------------------------------------------------    
    GROUP_BOT_SESSION = os.environ.get("GROUP_BOT_SESSION", True)
    APP_ID = os.environ.get("APP_ID", True)
    APP_HASH = os.environ.get("APP_HASH", True)
#------------------------------------------------------------------------------------------------------------------------------


    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

else:
    from UltronRoBo.sample_config import Development as UltronRoBo

    TOKEN = UltronRoBo.TOKEN

    try:
        OWNER_ID = int(UltronRoBo.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = UltronRoBo.JOIN_LOGGER
    OWNER_USERNAME = UltronRoBo.OWNER_USERNAME
    ALLOW_CHATS = UltronRoBo.ALLOW_CHATS
    try:
        DRAGONS = set(int(x) for x in UltronRoBo.DRAGONS or [])
        DEV_USERS = set(int(x) for x in UltronRoBo.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in UltronRoBo.DEMONS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in UltronRoBo.WOLVES or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in UltronRoBo.TIGERS or [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

   

    EVENT_LOGS = UltronRoBo.EVENT_LOGS
    WEBHOOK = UltronRoBo.WEBHOOK
    URL = UltronRoBo.URL
    PORT = UltronRoBo.PORT
    CERT_PATH = UltronRoBo.CERT_PATH
    API_ID = UltronRoBo.API_ID
    API_HASH = UltronRoBo.API_HASH

    DB_URI = UltronRoBo.SQLALCHEMY_DATABASE_URI
    MONGO_DB_URI = UltronRoBo.MONGO_DB_URI
    HEROKU_API_KEY = UltronRoBo.HEROKU_API_KEY
    HEROKU_APP_NAME = UltronRoBo.HEROKU_APP_NAME
    TEMP_DOWNLOAD_DIRECTORY = UltronRoBo.TEMP_DOWNLOAD_DIRECTORY
    OPENWEATHERMAP_ID = UltronRoBo.OPENWEATHERMAP_ID
    BOT_ID = UltronRoBo.BOT_ID
    VIRUS_API_KEY = UltronRoBo.VIRUS_API_KEY
    LOAD = UltronRoBo.LOAD
    NO_LOAD = UltronRoBo.NO_LOAD
    DEL_CMDS = UltronRoBo.DEL_CMDS
    STRICT_GBAN = UltronRoBo.STRICT_GBAN
    WORKERS = UltronRoBo.WORKERS
    BAN_STICKER = UltronRoBo.BAN_STICKER
    ALLOW_EXCL = UltronRoBo.ALLOW_EXCL
    CASH_API_KEY = UltronRoBo.CASH_API_KEY
    TIME_API_KEY = UltronRoBo.TIME_API_KEY
    AI_API_KEY = UltronRoBo.AI_API_KEY
    WALL_API = UltronRoBo.WALL_API
    SUPPORT_CHAT = UltronRoBo.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = UltronRoBo.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = UltronRoBo.SPAMWATCH_API
    INFOPIC = UltronRoBo.INFOPIC
    REDIS_URL = UltronRoBo.REDIS_URL
    GROUP_BOT_SESSION = UltronRoBo.GROUP_BOT_SESSION
    
    try:
        BL_CHATS = set(int(x) for x in UltronRoBo.BL_CHATS or [])
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1732236209)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")

UltronRoBot = TelegramClient(StringSession(GROUP_BOT_SESSION), API_ID, API_HASH)
try:
    UltronRoBot.start()
except BaseException:
    print("UserBot Error ! Did you add a GROUP_BOT_SESSION at the time of deploying??")
    sys.exit(1)

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("Ultron", API_ID, API_HASH)
UltronRobo = Client("UltronRoBo", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from UltronRoBo.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
