# MIT License
# Original project: https://github.com/Codeflix-Bots/FileStore
#
# This version is customized for Watch Drop brand.
# You MUST keep the MIT license header, but you are free to change configs, text, and branding.

import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler

# --------------------------------------------
# Bot Settings
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")   # Bot token from @BotFather
APP_ID = int(os.environ.get("APP_ID", "0"))         # API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")           # API Hash from my.telegram.org

# --------------------------------------------
# Owner / Channel Config
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))  # Your DB channel ID
OWNER = os.environ.get("OWNER", "watchdrop")         # Owner username (without @)
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))      # Owner user ID

# --------------------------------------------
# Server & Database
PORT = os.environ.get("PORT", "8001")
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "WatchDropBot")

# --------------------------------------------
# Other Settings
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 = no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/WatchDropSupport")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

# Images
START_PIC = os.environ.get("START_PIC", "")
FORCE_PIC = os.environ.get("FORCE_PIC", "")

# --------------------------------------------
# Messages (Customized for Watch Drop)
HELP_TXT = """
<b>📁 Watch Drop - FileStore Help</b>

❏ /start - Start the bot
❏ /about - About Watch Drop
❏ /help - Show help
"""

ABOUT_TXT = """
<b>ℹ️ About Watch Drop</b>

◈ Creator: <a href="https://t.me/watchdrop">Watch Drop</a>
◈ Brand: Watch Drop
◈ Main Channel: <a href="https://t.me/watchdropchannel">Watch Drop Channel</a>
◈ Support: <a href="https://t.me/watchdropsupport">Watch Drop Support</a>
"""

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>👋 Hello {mention},\n\nWelcome to <u>Watch Drop</u> File Store Bot.\nI can save your private files in a channel and give you special links to share them.</b>"
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "👋 Hello {mention},\n\n<b>Please join our official channels and then click 'Reload' to access your requested file.</b>"
)

CMD_TXT = """
<b>⚙️ Admin Commands</b>

/dlt_time - Set auto-delete time
/check_dlt_time - Check delete time
/dbroadcast - Broadcast document/video
/ban - Ban a user
/unban - Unban a user
/banlist - List banned users
/addchnl - Add force-sub channel
/delchnl - Remove force-sub channel
/listchnl - List force-sub channels
/fsub_mode - Toggle force-sub mode
/pbroadcast - Broadcast photo
/add_admin - Add an admin
/deladmin - Remove an admin
/admins - List admins
/delreq - Remove leftover non-request users
"""

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• Uploaded via Watch Drop</b>")
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⛔ Sorry, you are not allowed to use this bot!"

# --------------------------------------------
# Logging
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
