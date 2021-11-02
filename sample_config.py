import os

import logging

from logging.handlers import RotatingFileHandler

logging.basicConfig(

    level=logging.INFO,

    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",

    datefmt='%d-%b-%y %H:%M:%S',

    handlers=[

        RotatingFileHandler(

            "clonebot-ui.txt",

            maxBytes=50000000,

            backupCount=10

        ),

        logging.StreamHandler()

    ]

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org

    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org

    API_HASH = os.environ.get("API_HASH", "")

    # Authorized users to use this bot

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string

    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # Database URI

    DB_URI = os.environ.get("DATABASE_URL", "")

    # Dynamical change delay command. example for default: /delay 5 will set delay to 5 seconds.

    CHANGE_DELAY_COMMAND = os.environ.get("CHANGE_DELAY_COMMAND", "delay")

    # Delay between sending files

    DELAY_SECS = int(os.environ.get("DELAY_SECS", 10))

    # Copying file types default

    FILE_TYPES = set(x for x in os.environ.get("FILE_TYPES", "document video audio voice photo").split())

def LOGGER(name: str) -> logging.Logger:
    
    return logging.getLogger(name)
