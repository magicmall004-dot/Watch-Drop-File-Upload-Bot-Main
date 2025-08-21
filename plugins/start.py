from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_MSG, HELP_MSG, ABOUT_MSG, START_PIC, BAN_SUPPORT

@Client.on_message(filters.private & filters.command("start"))
async def start_handler(client, message):
    buttons = [
        [InlineKeyboardButton("📖 Help", callback_data="help"),
         InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("💬 Support", url=BAN_SUPPORT)]
    ]
    if START_PIC:
        await message.reply_photo(
            START_PIC,
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    else:
        await message.reply_text(
            START_MSG,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )

@Client.on_callback_query(filters.regex("help"))
async def help_cb(client, query):
    await query.message.edit_text(
        HELP_MSG,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Home", callback_data="home"),
             InlineKeyboardButton("ℹ️ About", callback_data="about")]
        ])
    )

@Client.on_callback_query(filters.regex("about"))
async def about_cb(client, query):
    await query.message.edit_text(
        ABOUT_MSG,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Home", callback_data="home"),
             InlineKeyboardButton("📖 Help", callback_data="help")]
        ])
    )

@Client.on_callback_query(filters.regex("home"))
async def home_cb(client, query):
    buttons = [
        [InlineKeyboardButton("📖 Help", callback_data="help"),
         InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("💬 Support", url=BAN_SUPPORT)]
    ]
    await query.message.edit_text(
        START_MSG,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
