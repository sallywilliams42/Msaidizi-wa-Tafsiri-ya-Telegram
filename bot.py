import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from googletrans import Translator
TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "Gtt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

@app.on_message(filters.private & filters.command(['start']))
async def start(client, message):
	await message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.message_id ,parse_mode="markdown", reply_markup=InlineKeyboardMarkup([ [                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],               [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]   ]  ) )
                  



@app.on_message(filters.private & filters.text  )
async def echo(client, message):

 
