import os
import asyncio
from aiohttp import web
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *
from plugins import web_server


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,  # fixed: you had APP_ID, but config.py uses API_ID
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # DB channel check
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            print(f"⚠️ Error: {e}")
            print(f"Make sure bot is Admin in DB Channel, and CHANNEL_ID={CHANNEL_ID}")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        print(f"✅ Bot @{usr_bot_me.username} started successfully!")

        # Start aiohttp web server (for Render free ping)
        app = await web_server()
        runner = web.AppRunner(app)
        await runner.setup()
        port = int(os.environ.get("PORT", 8080))  # Render provides PORT
        site = web.TCPSite(runner, "0.0.0.0", port)
        await site.start()
        print(f"🌐 Web server running on port {port}")

        # Notify Owner
        try:
            await self.send_message(OWNER_ID, "✅ Bot restarted successfully!")
        except:
            pass

    async def stop(self, *args):
        await super().stop()
        print("🛑 Bot stopped.")

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print("Shutting down...")
        finally:
            loop.run_until_complete(self.stop())


if __name__ == "__main__":
    Bot().run()
