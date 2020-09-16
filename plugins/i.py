from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time


@app.on_message(filters.command("start"))
async def forward(client, message):
 if message.from_user.id == 491634139:
   await message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   await message.reply("♻️ You need admins permission to use my functions. ✅✅")
