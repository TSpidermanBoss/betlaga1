from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time

@app.on_message(Filters.private)
async def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")
