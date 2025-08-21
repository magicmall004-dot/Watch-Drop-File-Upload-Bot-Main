# ==============================================================
# Watch Drop Bot - Broadcast System
# Copyright (c) 2025 Watch Drop
# Licensed under the MIT License
# ==============================================================

import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from bot import Bot
from config import *
from database.database import db
from plugins.admin import admin

REPLY_ERROR = "<b>Reply to a message to use this command.</b>"


# ---------------- PIN BROADCAST ----------------
@Bot.on_message(filters.private & filters.command('pbroadcast') & admin)
async def send_pin_text(client: Bot, message: Message):
    if not message.reply_to_message:
        return await message.reply(REPLY_ERROR, quote=True)

    query = await db.full_userbase()
    broadcast_msg = message.reply_to_message
    total = successful = blocked = deleted = unsuccessful = 0

    pls_wait = await message.reply("<i>Broadcast with pin processing....</i>")
    for chat_id in query:
        try:
            sent_msg = await broadcast_msg.copy(chat_id)
            await client.pin_chat_message(chat_id=chat_id, message_id=sent_msg.id, both_sides=True)
            successful += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            sent_msg = await broadcast_msg.copy(chat_id)
            await client.pin_chat_message(chat_id=chat_id, message_id=sent_msg.id, both_sides=True)
            successful += 1
        except UserIsBlocked:
            await db.del_user(chat_id)
            blocked += 1
        except InputUserDeactivated:
            await db.del_user(chat_id)
            deleted += 1
        except Exception as e:
            print(f"PBroadcast failed for {chat_id}: {e}")
            unsuccessful += 1
        total += 1

    await pls_wait.edit(f"""<b><u>📌 Pin Broadcast Completed</u></b>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked: <code>{blocked}</code>
Deleted: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code>""")


# ---------------- NORMAL BROADCAST ----------------
@Bot.on_message(filters.private & filters.command('broadcast') & admin)
async def send_text(client: Bot, message: Message):
    if not message.reply_to_message:
        return await message.reply(REPLY_ERROR, quote=True)

    query = await db.full_userbase()
    broadcast_msg = message.reply_to_message
    total = successful = blocked = deleted = unsuccessful = 0

    pls_wait = await message.reply("<i>Broadcast processing....</i>")
    for chat_id in query:
        try:
            await broadcast_msg.copy(chat_id)
            successful += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await broadcast_msg.copy(chat_id)
            successful += 1
        except UserIsBlocked:
            await db.del_user(chat_id)
            blocked += 1
        except InputUserDeactivated:
            await db.del_user(chat_id)
            deleted += 1
        except Exception as e:
            print(f"Broadcast failed for {chat_id}: {e}")
            unsuccessful += 1
        total += 1

    await pls_wait.edit(f"""<b><u>📢 Broadcast Completed</u></b>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked: <code>{blocked}</code>
Deleted: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code>""")


# ---------------- AUTO-DELETE BROADCAST ----------------
async def auto_delete(msg, delay):
    await asyncio.sleep(delay)
    try:
        await msg.delete()
    except:
        pass

@Bot.on_message(filters.private & filters.command('dbroadcast') & admin)
async def delete_broadcast(client: Bot, message: Message):
    if not message.reply_to_message:
        return await message.reply(REPLY_ERROR, quote=True)

    try:
        duration = int(message.command[1])
    except (IndexError, ValueError):
        return await message.reply("<b>Usage:</b> /dbroadcast {seconds}")

    query = await db.full_userbase()
    broadcast_msg = message.reply_to_message
    total = successful = blocked = deleted = unsuccessful = 0

    pls_wait = await message.reply("<i>Broadcast with auto-delete processing....</i>")
    for chat_id in query:
        try:
            sent_msg = await broadcast_msg.copy(chat_id)
            asyncio.create_task(auto_delete(sent_msg, duration))
            successful += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            sent_msg = await broadcast_msg.copy(chat_id)
            asyncio.create_task(auto_delete(sent_msg, duration))
            successful += 1
        except UserIsBlocked:
            await db.del_user(chat_id)
            blocked += 1
        except InputUserDeactivated:
            await db.del_user(chat_id)
            deleted += 1
        except Exception as e:
            print(f"DBroadcast failed for {chat_id}: {e}")
            unsuccessful += 1
        total += 1

    await pls_wait.edit(f"""<b><u>🗑️ Auto-Delete Broadcast Completed</u></b>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked: <code>{blocked}</code>
Deleted: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code>""")
