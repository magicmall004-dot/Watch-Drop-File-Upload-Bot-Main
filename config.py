import os

# Telegram API credentials
API_ID = int(os.environ.get("APP_ID", "21404189"))
API_HASH = os.environ.get("API_HASH", "bd7028cc6f1bad77cd8e53023bf895b6")

# Bot token
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8434337760:AAFKQvjOHBFTiM_zdz-jaDgR_J8YdPl7Iow")

# Database channel
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002973651102"))  # Your DB channel ID

# Owner info
OWNER = os.environ.get("OWNER", "Magic_Mall_GameShop")   # Without @
OWNER_ID = int(os.environ.get("OWNER_ID", "1849257766"))

# Database URL (Mongo/Postgres depending on your setup)
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Flame:HtunHlaAung-007047@watch-drop.cmn22zb.mongodb.net/?retryWrites=true&w=majority&appName=WATCH-DROP")

# Support group link
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/MagicMallCustomerSupportBot")

# Optional branding images
START_PIC = os.environ.get("START_PIC", "")
FORCE_PIC = os.environ.get("FORCE_PIC", "")

# Custom caption footer
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "• ʙʏ @WatchDrop")

# File protect
PROTECT_CONTENT = bool(os.environ.get("PROTECT_CONTENT", False))

# Fsub expiry
FSUB_LINK_EXPIRY = int(os.environ.get("FSUB_LINK_EXPIRY", "10"))

# Text templates
START_MSG = """
👋 Welcome to **Watch Drop**!

I can store files in my database and share them with permanent links.  
Just send me any media and I’ll save it for you.

Use me in your groups too — I can auto-reply with files.

⚙️ Use /help to see available commands.
"""

HELP_MSG = """
📖 **Watch Drop Help**

• Send me any file — I’ll save it and give you a permanent shareable link.  
• Add me to your groups — I’ll respond to file requests automatically.

🔒 Admin commands (for bot owner):
/commands — show admin command list
/addchnl /delchnl /listchnl — manage force-sub channels
/ban /unban /banlist — manage bans
/broadcast — send message to all users

❓ Need help? Contact support: @MagicMallCustomerSupportBot
"""

ABOUT_MSG = """
**🤖 Bot:** Watch Drop FileStore  
**👨‍💻 Owner:** @{OWNER}  
**📢 Updates:** @watch_drop_movies_and_series  
**💬 Support:** @MagicMallCustomerSupportBot
"""
