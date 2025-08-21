from aiohttp import web
from plugins import web_server
import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,   # ✅ fixed (was APP_ID)
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="✅ Bot Connected Successfully!")
            await test.delete()
        except Exception as e:
            print(f"[ERROR] {e}")
            print(f"❌ Make sure bot is Admin in DB Channel (ID: {CHANNEL_ID})")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        print(f"🤖 Bot @{usr_bot_me.username} started successfully!")

        # Start web server (needed for Render + UptimeRobot pings)
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

        try:
            await self.send_message(OWNER_ID, text="<b>✅ Bot Restarted and is now Online!</b>")
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
            print("⚠️ Shutting down...")
        finally:
            loop.run_until_complete(self.stop())


if __name__ == "__main__":
    Bot().run()
