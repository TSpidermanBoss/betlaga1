from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time

@app.on_message(filters.command('list') & filters.user(491634139))
async def forward(client, message):
  file = open(message.text.split(" ")[1] + ".txt" , "r")
  u = file.readlines()
  file.close()
  for v in u :
      await message.reply("🏘️ List of Chat_ids in my database are ```" + str(v) + "```. Its can be change. ✅✅")
